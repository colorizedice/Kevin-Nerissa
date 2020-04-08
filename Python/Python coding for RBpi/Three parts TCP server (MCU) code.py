import socket
import random
import time

tcp_ip_address = '0.0.0.0' 
tcp_port = 5015
buffer_size = 20

ser1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ser1.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
ser1.bind((tcp_ip_address, tcp_port))
ser1.listen(2)

#accept() returns an open connection between the server and client, along with the address of the client. The connection is actually
#a different socket on another port (assigned by the Kernel). Data is read from the connection with recv() and transmitted with sendall()

connection, addr = ser1.accept()
print("Client address is: ", addr)

for i in range(1,11):
    try:
        error_simulation = random.randint(1,101)
        data_from_testingPC = connection.recv(buffer_size)
        if (data_from_testingPC == b"yes"):
            connection.send(str(error_simulation).encode())
            time.sleep(1)
        else:
            print("No more data from client!")
#            break
    except KeyboardInterrupt:
        connection.close()
        break
    
connection.close()
ser1.close()
