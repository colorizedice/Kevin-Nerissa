# This code is for SRAM by MCU communication

import socket
import time
import sys

port_MCU = 5000
Ipaddr_MCU = '192.168.0.123'

ser_MCU = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#ser_MCU.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE,1)
ser_MCU.connect((Ipaddr_MCU,port_MCU))

server_UDPsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_UDPsocket.bind(('', 61558))

RX = [0]*257

    #data_pattern can be 0, 1, 10 or 11
data_pattern = 1

    #data_compare is used to test if there is an error
data_compare = 0

    #test_round is the number that how many rounds the testing code will run. It should be in range of [0,255]
    #test_round = 0

#    try:
        
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

test_round = 2

TX[2] = test_round

print("the configuration list TX is: " + str(TX))
            
    #	ser_MCU.send(b'8501000')

ser_MCU.sendall(bytes(TX))

while True:
    a = input("yes or no: ")
    if a== 'y' :
        break
   
   
            
TX[0] = 31
#while True:
#    message, address = server_UDPsocket.recvfrom(16)
#    print('The received info is %s.'%message)
#    if message == b'yes':
#        break
print('The trigger configuration list is: ' + str(TX))

ser_MCU.sendall(bytes(TX))
            
  
err_sum = 0
    
#	rx = ser_MCU.recv(5000)
#	print(rx)
    
#        for i in range(8):    
while True:            
    RX = ser_MCU.recv(257)
    '''
    if RX[0]==2:
        print(RX[0])
        print(RX)
     '''        

    for j in range (256):
        #if(i != 0 and i%257 != 0):
        err_number = RX[j+1]^ data_compare
        
        err_number_binary = bin(err_number).count('1')
        
        '''
        if err_number_binary != 0:
                    addr_num = RX[0]*256 + j
                   
                    print("Round start! \n")
                    print("Page[%d]----Addr: %d ----Err: %s \n" %(RX[0], addr_num, bin(err_number)))
          '''          
                
        
        err_sum = err_number_binary + err_sum
        
    if RX[0] == 7:
        break
                  

print('The total number of generated errors is: ' + str(err_sum))
        
#        j = j+1
        
        
#        time.sleep(1)



#    except KeyboardInterrupt:
#        ser_MCU.shutdown()
#        ser_MCU.close()
#        print('Connection is closed!')




