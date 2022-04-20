from socket import socket, AF_INET, SOCK_DGRAM
udp_soc = socket(AF_INET, SOCK_DGRAM)
udp_soc.bind(('127.0.0.1', 8080))

while True:
    data, addr = udp_soc.recvfrom(200)
    print(f'recv from {addr} : {data}')
    temp_data = data
    data = data.decode().upper()
    print(f'data is {temp_data} and')
    print(f'change to {data}')
    udp_soc.sendto(data.encode(), addr)

udp_soc.close()
