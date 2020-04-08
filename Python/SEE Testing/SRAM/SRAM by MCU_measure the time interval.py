# This code is for SRAM by MCU communication

import socket
import time
import sys

'''port_MCU = 5000
Ipaddr_MCU = '192.168.0.123'

ser_MCU = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ser_MCU.connect((Ipaddr_MCU,port_MCU))'''


while True:

    port_MCU = 5000
    Ipaddr_MCU = '192.168.0.123'
    buffer_size = 1

    #server_UDPsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #server_UDPsocket.bind(('', 61557))

    ser_MCU = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ser_MCU.connect((Ipaddr_MCU,port_MCU))

    #data_pattern can be 0, 1, 10 or 11
    data_pattern = 0

    #data_compare is used to test if there is an error
    data_compare = 0

    #test_round is the number that how many rounds the testing code will run. It should be in range of [0,255]
    #test_round = 0

    try:
        
        print('Connection to MCU has been built!')
        TX = [0]*6
    #	RX = [None]*2056

    # send configuration info to fpga

        TX[0] = 85
        if (data_pattern == 0):
                TX[1] = 0
                data_compare = 0
        elif (data_pattern == 1):
                TX[1] = 1
                data_compare = 85
        elif (data_pattern == 10):
                TX[1] = 2
                data_compare = 170
        elif (data_pattern == 11):
                TX[1] = 3
                data_compare = 255

        test_round = 1

        TX[2] = test_round

        print("the configuration list TX is: " + str(TX))
            
    #	ser_MCU.send(b'8501000')

        ser_MCU.sendall(bytes(TX))
    #	for data in TX:
    #	    ser_MCU.send(bytes(data))
    #        message, address = server_UDPsocket.recvfrom(64)
            #message = message.upper()
    #        print('The received info is %s.'%message)
            
    #        if message == b'yes':
            
        TX[0] = 31
        print('The trigger configuration list is: ' + str(TX))
        
        ser_MCU.sendall(bytes(TX))
            
            
            
    #	ser_MCU.send(b'3101000')
            
    #	for data in TX:
    #           ser_MCU.send(bytes(data))
            

    # From here, the code starts to count the error number

    #	loop_number = 0 # this number is in range of [0, test_round]
    #	address = 0  #output sequence
            
            
            
            
            
        err_sum = 0
            
    #	rx = ser_MCU.recv(5000)
    #	print(rx)
            
            
        for i in range (2056):        
            rx = ser_MCU.recv(1)
            rx_int = int.from_bytes(rx,'big')
    #        rx_int = ord(rx)
    #	    RX[i] = int(rx)
    #	    print(rx)
            if(i != 0 and i%257 != 0):
                err_number = rx_int ^ data_compare
                err_number_binary = bin(err_number).count('1')
                err_sum = err_number_binary + err_sum

                
                        

    #	for j in range (2056):
    #            if (j != 0 and j%257 != 0):

    #                if(RX[j] != data_compare):

    #                err_number = RX[j] ^ data_compare
    #               err_number_binary = bin(err_number).count('1')
    #                err_sum = err_number_binary + err_sum

    #        returnmessage = str(err_sum)
    #        server_socket.sendto(returnmessage.encode(), address)
                

        print('The total number of generated errors is: ' + str(err_sum))
        
        
        time.sleep(1.4)



    except KeyboardInterrupt:
#        ser_MCU.shutdown()
#        ser_MCU.close()
        print('Connection is closed!')

