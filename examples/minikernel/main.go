package main

import (
	"flag"
	"fmt"
	"log"
	"net"
	"os"
	"os/signal"
	"time"
)

// main starts one node. Run two instances to see the minimal kernel work:
//
//	go run . -listen 127.0.0.1:6024
//	go run . -listen 127.0.0.1:6025 -peer 127.0.0.1:6024 -msg "hello"
func main() {
	listen := flag.String("listen", "127.0.0.1:6024", "UDP address to bind")
	peer := flag.String("peer", "", "optional peer UDP address to handshake with")
	msg := flag.String("msg", "", "optional message to send after handshake")
	flag.Parse()

	node, err := NewNode()
	if err != nil {
		log.Fatalf("identity: %v", err)
	}
	t, err := NewTransport(node, *listen)
	if err != nil {
		log.Fatalf("listen: %v", err)
	}
	defer t.Close()
	fmt.Printf("node %s listening on %s\n", node.ID, t.Addr())

	if *peer != "" {
		addr, err := net.ResolveUDPAddr("udp", *peer)
		if err != nil {
			log.Fatalf("peer address: %v", err)
		}
		id, err := t.Hello(addr, 5*time.Second)
		if err != nil {
			log.Fatalf("handshake: %v", err)
		}
		fmt.Printf("handshake ok with %s\n", id)
		if *msg != "" {
			if err := t.SendMessage(addr, *msg); err != nil {
				log.Fatalf("send: %v", err)
			}
			fmt.Printf("sent: %q\n", *msg)
		}
	}

	stop := make(chan os.Signal, 1)
	signal.Notify(stop, os.Interrupt)
	for {
		select {
		case m := <-t.Inbox():
			fmt.Printf("received from %s: %q\n", m.From, m.Payload)
		case <-stop:
			fmt.Println("shutdown")
			return
		}
	}
}
