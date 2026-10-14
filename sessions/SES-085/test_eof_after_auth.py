"""Regression coverage for EOF after a valid authenticated handshake."""

import socket
import threading

from src.p2p import P2PNode
from src.p2p.node import _receive_line
from src.p2p.protocol import (
    auth,
    auth_payload,
    hello,
    parse_welcome,
    verify_signature,
)


def test_listener_rejects_eof_after_auth_before_application_frame():
    server = P2PNode("B")
    client = P2PNode("A")
    result = {}

    def serve():
        try:
            result["response"] = server.listen_once()
        except Exception as exc:
            result["error"] = exc

    thread = threading.Thread(target=serve)
    thread.start()

    try:
        with socket.create_connection(
            ("127.0.0.1", server.bound_port), timeout=2
        ) as conn:
            client_challenge = b"c" * 32
            conn.sendall(
                (
                    hello(
                        client.node_id,
                        client.public_key,
                        client_challenge,
                        client.label,
                    )
                    + "\n"
                ).encode("utf-8")
            )

            buffer = bytearray()
            peer_id, peer_public_key, server_challenge, server_signature = (
                parse_welcome(_receive_line(conn, buffer))
            )
            verify_signature(
                peer_public_key,
                server_signature,
                auth_payload(client.node_id, peer_id, client_challenge),
            )

            signature = client._identity_key.sign(
                auth_payload(client.node_id, server.node_id, server_challenge)
            )
            conn.sendall((auth(signature) + "\n").encode("utf-8"))
            # Closing here simulates a peer disconnecting after AUTH but
            # before sending any complete application frame.

        thread.join(timeout=3)

        assert not thread.is_alive(), "listener did not finish after peer EOF"
        assert isinstance(result.get("error"), ValueError)
        assert "incomplete frame" in str(result["error"])
        assert server.last_peer_id == client.node_id
        assert server.last_message is None
    finally:
        server.close()
        client.close()
        if thread.is_alive():
            thread.join(timeout=1)
