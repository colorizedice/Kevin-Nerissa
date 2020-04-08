import socket
import time
import random
import sys

tcp_ip_address = "192.168.0.122"
port = 6340
buffer_size = 20
#error_number = "23 \r\n"
#message = "Hi, bro. It's me again and again and again.\n"
#message2 ="hahaha. \r\n"


ser = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
'''
x=ser.getsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE)
if(x==0):
    print("Socket keepalive is off, turning it on!")
    x=ser.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE,1)
'''
ser.connect((tcp_ip_address, port))

while True:
    try:
#        error = random.randint(1,101)
#        ser.send(str(error).encode())
        data_from_server = ser.recv(buffer_size)
        if(data_from_server!=b""):
            print(data_from_server)
        if (data_from_server == b"yes"):
            TX = [1,2,3,4]
            ser.sendall(bytes(TX))
#            for i in TX:
#                ser.send(bytes[i])
            time.sleep(1)
    except KeyboardInterrupt:
        print("connection is closed!")
        ser.close()
        break
    #ser.send(error_number.encode())
#    ser.send(message2.encode())
#else:
#    ser.send(message.encode())
#    print("Nothing was sent to Server")


#time.sleep(1)

ser.close()

#print("Received data from server : ", data)