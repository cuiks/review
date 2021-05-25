# -*- coding: utf-8 -*-

import socket


def server():
    # 创建socket
    s = socket.socket()
    host = "127.0.0.1"
    port = 6666
    # 绑定套接字
    s.bind((host, port))

    # 监听
    s.listen(5)

    while True:
        c, addr = s.accept()
        print("Connect Addr", addr)
        c.send(b"Welcome")
        c.close()


if __name__ == '__main__':
    server()
