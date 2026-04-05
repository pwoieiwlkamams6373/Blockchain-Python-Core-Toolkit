import socket
import threading

class P2PNode:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.peers = []

    def start_server(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((self.host, self.port))
        server.listen(5)
        print(f"P2P节点启动: {self.host}:{self.port}")
        while True:
            conn, addr = server.accept()
            threading.Thread(target=self.handle_peer, args=(conn,)).start()

    def handle_peer(self, conn):
        while True:
            data = conn.recv(1024)
            if not data: break
            print("收到消息:", data.decode())
        conn.close()

if __name__ == "__main__":
    node = P2PNode("127.0.0.1", 8888)
    threading.Thread(target=node.start_server).start()
