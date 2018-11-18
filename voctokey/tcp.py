import socket


class TcpClient():
    def __init__(self, ip, port):
        self.bufsize = 1024
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((ip, int(port)))

    def send(self, msg):
        self.socket.send(msg)
        return self.socket.recv(self.bufsize)

    def close(self):
        self.socket.close()
