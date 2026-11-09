package main

import (
	"crypto/ed25519"
	"encoding/json"
	"net"
	"testing"
	"time"
)

// newPair starts two transports on loopback with free ports.
func newPair(t *testing.T) (*Transport, *Transport) {
	t.Helper()
	a, err := NewNode()
	if err != nil {
		t.Fatal(err)
	}
	b, err := NewNode()
	if err != nil {
		t.Fatal(err)
	}
	ta, err := NewTransport(a, "127.0.0.1:0")
	if err != nil {
		t.Fatal(err)
	}
	tb, err := NewTransport(b, "127.0.0.1:0")
	if err != nil {
		t.Fatal(err)
	}
	t.Cleanup(func() { ta.Close(); tb.Close() })
	return ta, tb
}

func TestHandshakeAndMessage(t *testing.T) {
	a, b := newPair(t)

	id, err := a.Hello(b.Addr(), 2*time.Second)
	if err != nil {
		t.Fatalf("handshake: %v", err)
	}
	if id != b.node.ID {
		t.Fatalf("handshake returned %q, want %q", id, b.node.ID)
	}

	if err := a.SendMessage(b.Addr(), "ping"); err != nil {
		t.Fatalf("send: %v", err)
	}
	select {
	case m := <-b.Inbox():
		if m.Payload != "ping" || m.From != a.node.ID {
			t.Fatalf("got %+v, want payload ping from %s", m, a.node.ID)
		}
	case <-time.After(2 * time.Second):
		t.Fatal("message not received")
	}
}

func TestHandshakeTimeout(t *testing.T) {
	a, _ := newPair(t)
	// Port 1 on loopback has no listener, so no ack can arrive.
	dead := &net.UDPAddr{IP: net.IPv4(127, 0, 0, 1), Port: 1}
	if _, err := a.Hello(dead, 300*time.Millisecond); err == nil {
		t.Fatal("expected handshake timeout")
	}
}

// rawSend writes an arbitrary datagram to dst from a fresh socket.
func rawSend(t *testing.T, dst *net.UDPAddr, data []byte) {
	t.Helper()
	c, err := net.DialUDP("udp", nil, dst)
	if err != nil {
		t.Fatal(err)
	}
	defer c.Close()
	if _, err := c.Write(data); err != nil {
		t.Fatal(err)
	}
}

// expectNothing asserts the inbox stays empty for a short window.
func expectNothing(t *testing.T, tr *Transport) {
	t.Helper()
	select {
	case m := <-tr.Inbox():
		t.Fatalf("accepted invalid message: %+v", m)
	case <-time.After(300 * time.Millisecond):
	}
}

func TestRejectTamperedPayload(t *testing.T) {
	a, b := newPair(t)
	m := Message{Type: TypeMsg, From: a.node.ID, FromKey: a.node.PubKey, Payload: "ok"}
	m.Sig = ed25519.Sign(a.node.privKey, signedBytes(&m))
	m.Payload = "evil" // altered after signing
	data, _ := json.Marshal(m)
	rawSend(t, b.Addr(), data)
	expectNothing(t, b)
}

func TestRejectSpoofedID(t *testing.T) {
	a, b := newPair(t)
	// Valid signature by a's key, but From claims a different ID.
	m := Message{Type: TypeMsg, From: "ffffffffffffffff", FromKey: a.node.PubKey, Payload: "x"}
	m.Sig = ed25519.Sign(a.node.privKey, signedBytes(&m))
	data, _ := json.Marshal(m)
	rawSend(t, b.Addr(), data)
	expectNothing(t, b)
}

func TestRejectGarbage(t *testing.T) {
	_, b := newPair(t)
	rawSend(t, b.Addr(), []byte("not json"))
	expectNothing(t, b)
}
