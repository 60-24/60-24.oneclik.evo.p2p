package main

import (
	"crypto/ed25519"
	"crypto/rand"
	"crypto/sha256"
	"encoding/hex"
)

// Node is an independent participant identified by its ed25519 public key.
// The private key never leaves this struct (CLAUDE.md §14: nie eksponuj PrivKey).
type Node struct {
	ID      string
	PubKey  ed25519.PublicKey
	privKey ed25519.PrivateKey
}

// NewNode generates a fresh identity.
func NewNode() (*Node, error) {
	pub, priv, err := ed25519.GenerateKey(rand.Reader)
	if err != nil {
		return nil, err
	}
	return &Node{ID: idFromKey(pub), PubKey: pub, privKey: priv}, nil
}

// idFromKey derives a stable node ID from a public key.
// The ID is bound to the key, so a peer cannot claim an ID it does not own.
func idFromKey(pub ed25519.PublicKey) string {
	sum := sha256.Sum256(pub)
	return hex.EncodeToString(sum[:8])
}
