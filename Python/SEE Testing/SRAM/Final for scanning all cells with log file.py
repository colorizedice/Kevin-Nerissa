# This code is for SRAM by MCU communication

import socket
import time
import sys

port_MCU = 5000
Ipaddr_MCU = '192.168.0.123'

ser_MCU = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#ser_MCU.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE,1)
ser_MCU.connect((Ipaddr_MCU,port_MCU))

'''
server_UDPsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_UDPsocket.bind(('', 61558))
'''

RX = [0]*257

#Create a log file to record the address and errors

StartTime = time.strftime("%Y_%m_%d_%I:%M:%S", time.gmtime())

dfile = open("/home/pi/SEE Testing/SRAM/Log_files/%s.txt" %(StartTime),"w+")

while True:
 
    buffer_size = 1 #this is the size that the RPI read from MCU


    #data_pattern can be 0, 1, 10 or 11. 0 means all zero; 1 means all one; 10 means zero and one; 11 means self-check
    data_pattern = 1

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

        test_round = 255

        TX[2] = test_round

        print("the configuration list TX is: " + str(TX))
            
    #	ser_MCU.send(b'8501000')

        ser_MCU.sendall(bytes(TX))
        while True:
            a = input("yes or no: ")
            if a== 'y' :
                break
        
    #	for data in TX:
    #	    ser_MCU.send(bytes(data))
    #        message, address = server_UDPsocket.recvfrom(64)
            #message = message.upper()
    #        print('The received info is %s.'%message)
            
    #        if message == b'yes':
            
        TX[0] = 31 #this is the trigger signal
        '''
        while True:
            message, address = server_UDPsocket.recvfrom(16)
            print('The received info is %s.'%message)
            if message == b'yes':
                break
        print('The trigger configuration list is: ' + str(TX))
        '''
        
        ser_MCU.sendall(bytes(TX))
    
            
            
            
    #	ser_MCU.send(b'3101000')
            
    #	for data in TX:
    #           ser_MCU.send(bytes(data))
            

    # From here, the code starts to count the error number

    #	loop_number = 0 # this number is in range of [0, test_round]
    #	address = 0  #output sequence
            
            
            
            
            
        err_sum = 0
        
        while True:
            RX = ser_MCU.recv(257)
            dfile = open("/home/pi/SEE Testing/SRAM/Log_files/%s.txt" %(StartTime),"a")
            '''
                Page 0: address 0---256
                Page 1: address 257---513
                Page 2: address 514---770
                Page 3: address 771---1027
                Page 4: address 1028---1284 SRAM: Quatro
                Page 5: address 1285---1541
                Page 6: address 1542---1798
                Page 7: address 1799---2055
            '''
            #if RX[0] == 4:
                
            for i in range (256):
                err_number = RX[i+1]^ data_compare
                
                err_number_binary = bin(err_number).count('1')
                
                if err_number_binary != 0:
                    addr_num = RX[0]*256 + i
                   
                    dfile.write("Round start! \r\n")
                    dfile.write("Page[%d]----Addr: %d ----Err: %s \r\n" %(RX[0], addr_num, bin(err_number)))
                    
                
                err_sum = err_number_binary + err_sum
            
            if RX[0] == 7:
                dfile.write("Round end! \r\n")
                dfile.write("\r\n")
                dfile.close()
                break
            

 #       server_UDPsocket.sendto(str(err_sum).encode(), address)
                

        print('The total number of generated errors is: ' + str(err_sum))
        
             
        time.sleep(0.1)



    except KeyboardInterrupt:
#        ser_MCU.shutdown()
#        ser_MCU.close()
        print('Connection is closed!')




