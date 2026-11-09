package main

import (
	"crypto/ed25519"
	"encoding/json"
	"errors"
	"net"
	"time"
)

// Message types of the minimal kernel (P2P_PROTOCOL_v0.1: handshake + message).
const (
	TypeHello = "hello"
	TypeAck   = "ack"
	TypeMsg   = "msg"
)

const maxDatagram = 4096

// ErrInvalidMessage is returned for datagrams that fail structural or signature checks.
var ErrInvalidMessage = errors.New("invalid message")

// Message is a signed UDP datagram.
type Message struct {
	Type    string `json:"type"`
	From    string `json:"from"`
	FromKey []byte `json:"from_key"`
	Payload string `json:"payload"`
	Sig     []byte `json:"sig"`
}

// signedBytes is the canonical byte form that the signature covers.
func signedBytes(m *Message) []byte {
	return []byte(m.Type + "\n" + m.From + "\n" + m.Payload)
}

// decodeVerified parses a datagram and checks that the sender ID matches the
// key and that the signature is valid. Anything else is rejected.
func decodeVerified(data []byte) (*Message, error) {
	var m Message
	if err := json.Unmarshal(data, &m); err != nil {
		return nil, ErrInvalidMessage
	}
	if len(m.FromKey) != ed25519.PublicKeySize {
		return nil, ErrInvalidMessage
	}
	pub := ed25519.PublicKey(m.FromKey)
	if idFromKey(pub) != m.From {
		return nil, ErrInvalidMessage
	}
	if !ed25519.Verify(pub, signedBytes(&m), m.Sig) {
		return nil, ErrInvalidMessage
	}
	return &m, nil
}

// Transport is a UDP endpoint bound to one node.
type Transport struct {
	node  *Node
	conn  *net.UDPConn
	inbox chan Message
	acks  chan string
}

// NewTransport binds a UDP socket. Use "127.0.0.1:0" to pick a free port.
func NewTransport(node *Node, addr string) (*Transport, error) {
	laddr, err := net.ResolveUDPAddr("udp", addr)
	if err != nil {
		return nil, err
	}
	conn, err := net.ListenUDP("udp", laddr)
	if err != nil {
		return nil, err
	}
	t := &Transport{
		node:  node,
		conn:  conn,
		inbox: make(chan Message, 64),
		acks:  make(chan string, 16),
	}
	go t.loop()
	return t, nil
}

// Addr returns the bound local address.
func (t *Transport) Addr() *net.UDPAddr {
	return t.conn.LocalAddr().(*net.UDPAddr)
}

// Inbox delivers verified application messages.
func (t *Transport) Inbox() <-chan Message {
	return t.inbox
}

// Close stops the transport. Safe to call once.
func (t *Transport) Close() error {
	return t.conn.Close()
}

// Hello performs the handshake with the peer at addr and returns its node ID.
// It retransmits the hello every 100 ms until an ack arrives or timeout expires.
func (t *Transport) Hello(addr *net.UDPAddr, timeout time.Duration) (string, error) {
	deadline := time.After(timeout)
	tick := time.NewTicker(100 * time.Millisecond)
	defer tick.Stop()
	for {
		if err := t.send(addr, TypeHello, ""); err != nil {
			return "", err
		}
		select {
		case id := <-t.acks:
			return id, nil
		case <-tick.C:
		case <-deadline:
			return "", errors.New("handshake timeout")
		}
	}
}

// SendMessage sends a signed application message to addr.
func (t *Transport) SendMessage(addr *net.UDPAddr, payload string) error {
	return t.send(addr, TypeMsg, payload)
}

// send builds, signs and transmits one datagram.
func (t *Transport) send(addr *net.UDPAddr, typ, payload string) error {
	m := Message{
		Type:    typ,
		From:    t.node.ID,
		FromKey: t.node.PubKey,
		Payload: payload,
	}
	m.Sig = ed25519.Sign(t.node.privKey, signedBytes(&m))
	data, err := json.Marshal(m)
	if err != nil {
		return err
	}
	if len(data) > maxDatagram {
		return errors.New("payload too large")
	}
	_, err = t.conn.WriteToUDP(data, addr)
	return err
}

// loop reads datagrams until the socket is closed.
func (t *Transport) loop() {
	buf := make([]byte, maxDatagram)
	for {
		n, raddr, err := t.conn.ReadFromUDP(buf)
		if err != nil {
			return
		}
		m, err := decodeVerified(buf[:n])
		if err != nil {
			continue // drop silently: unverified input never reaches the node
		}
		switch m.Type {
		case TypeHello:
			_ = t.send(raddr, TypeAck, "")
		case TypeAck:
			select {
			case t.acks <- m.From:
			default:
			}
		case TypeMsg:
			select {
			case t.inbox <- *m:
			default: // inbox full: drop, never block the socket loop
			}
		}
	}
}
