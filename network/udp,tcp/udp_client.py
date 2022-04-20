from socket import socket, AF_INET, SOCK_DGRAM
udp_soc = socket(AF_INET, SOCK_DGRAM)

while True:
    msg = input("->")
    udp_soc.sendto(msg.encode(), ('127.0.0.1', 8080))
    recvMsg, addr = udp_soc.recvfrom(8080)
    print(recvMsg.decode(), addr)

udp_soc.close()