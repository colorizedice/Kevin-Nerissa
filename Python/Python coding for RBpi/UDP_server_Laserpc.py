import random
import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('', 61558))

i = 0

while True:
    message, address = server_socket.recvfrom(64)
#    message = message.upper()
    print('The received info is %s.'%message)
    
#    if message == b'yes':
    while True:
        if message == b'yes':
            break
    returnmessage = "hello world " + str(i)
    server_socket.sendto(returnmessage.encode(), address)
        
    i = i+1