from socket import socket, AF_INET, SOCK_STREAM
tcp_sock = socket(AF_INET, SOCK_STREAM)
tcp_sock.connect(('127.0.0.1', 8080))

while True:
    msg = input("->")
    tcp_sock.send(msg.encode())
    data = tcp_sock.recv(1024)
    print(data.decode())

tcp_sock.close()