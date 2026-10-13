import socket
import threading

from src.p2p import P2PNode
from src.p2p.protocol import auth, auth_payload, hello, parse_welcome, verify_signature


def test_listener_rejects_carriage_return_in_inbound_application_message():
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
            stream = conn.makefile("rb")
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
                stream.readline().decode("utf-8").rstrip("\n")
            )
            verify_signature(
                peer_public_key,
                server_signature,
                auth_payload(client.node_id, peer_id, client_challenge),
            )
            signature = client._identity_key.sign(
                auth_payload(client.node_id, server.node_id, server_challenge)
            )
            conn.sendall(
                (auth(signature) + "\n" + "first\rsecond\n").encode("utf-8")
            )
            stream.close()

        thread.join(timeout=3)
        assert not thread.is_alive()
        assert isinstance(result.get("error"), ValueError)
        assert str(result["error"]) == "message must be a single line"
        assert server.last_message is None
    finally:
        server.close()
        client.close()
        if thread.is_alive():
            thread.join(timeout=1)
