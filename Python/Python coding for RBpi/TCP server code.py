import socket

tcp_ip_address = '0.0.0.0' #ip address of the pi is : 10.81.8.10
tcp_port = 5005
buffer_size = 20

ser = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ser.bind((tcp_ip_address, tcp_port))
ser.listen(2)

#accept() returns an open connection between the server and client, along with the address of the client. The connection is actually
#a different socket on another port (assigned by the Kernel). Data is read from the connection with recv() and transmitted with sendall()

connection, addr = ser.accept()
print("Client address is: ", addr)

while True:
    try:
        data = connection.recv(buffer_size)
        if data:
            print("Sending back to Client!")
            connection.send(data)
        else:
            print("No more data from client!")
#            break
    except KeyboardInterrupt:
        connection.close()
        break
    
connection.close()