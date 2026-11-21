import socket
import threading

from src.p2p import P2PNode
from src.p2p.protocol import (
    auth,
    auth_payload,
    hello,
    message_payload,
    msg,
    node_id_from_public_key,
    parse_welcome,
    session_id,
    verify_signature,
)

# SES-090 update: after AUTH the application line is now a signed ``MSG`` frame
# (message integrity, handshake context V2). This test originally sent a plain
# text line. It is updated, not retired: its purpose is unchanged - AUTH and the
# application frame arrive in ONE TCP segment and the listener must keep the
# bytes after the first delimiter. Only the frame format changed.


def test_listener_preserves_bytes_after_first_delimiter():
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
        with socket.create_connection(("127.0.0.1", server.bound_port), timeout=2) as conn:
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

            peer_id, peer_public_key, server_challenge, server_signature = parse_welcome(
                conn.recv(4096).decode("utf-8").rstrip("\n")
            )
            verify_signature(
                peer_public_key,
                server_signature,
                auth_payload(client.node_id, peer_id, client_challenge),
            )

            signature = client._identity_key.sign(
                auth_payload(client.node_id, server.node_id, server_challenge)
            )
            message_signature = client._identity_key.sign(
                message_payload(
                    session_id(
                        client.node_id, server.node_id, client_challenge, server_challenge
                    ),
                    client.node_id,
                    server.node_id,
                    1,
                    "coalesced-message",
                )
            )
            conn.sendall(
                (
                    auth(signature)
                    + "\n"
                    + msg(1, message_signature, "coalesced-message")
                    + "\n"
                ).encode("utf-8")
            )

        thread.join(timeout=3)

        assert not thread.is_alive()
        assert result == {"response": "pong-from-B"}
        assert server.last_peer_id == client.node_id
        assert server.last_message == "coalesced-message"
    finally:
        server.close()
        client.close()
        if thread.is_alive():
            thread.join(timeout=1)
