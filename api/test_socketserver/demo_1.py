# coding=utf-8
import socketserver


class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    测试demo
    """
    def handle(self):
        self.data = self.request.recv(1024).strip()
        print("{} wrote:".format(self.client_address))
        print(self.data)

        self.request.sendall(self.data.upper())


if __name__ == '__main__':
    HOST,PORT = "localhost", 9999
    sever = socketserver.TCPServer((HOST, PORT), MyTCPHandler)

    sever.serve_forever()