from socket import socket, AF_INET, SOCK_STREAM
tcp_sock = socket(AF_INET, SOCK_STREAM)
tcp_sock.bind(('127.0.0.1', 8080))
tcp_sock.listen()
con, addr = tcp_sock.accept()

while True:
    data = con.recv(1024).decode()
    if not data:
        break
    print(f'recv data {data}')
    sdata = data.upper()
    print(f'{data} change to {sdata} and send to client')
    con.send(sdata.encode())

tcp_sock.close()