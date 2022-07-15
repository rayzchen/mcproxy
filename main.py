import socket

with open("server.txt") as f:
    host, port = f.read().rstrip().split(":")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(("127.0.0.1"), 25565)
    s.listen()
    conn, addr = s.accept()
    with conn:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s2:
            s2.connect((host, port))
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                s2.sendall(data)

