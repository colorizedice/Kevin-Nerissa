# This code is for SRAM by MCU communication

import socket
import time
import sys

port_MCU = 5000
Ipaddr_MCU = '192.168.0.123'
buffer_size = 1

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
	TX = [0]*10
	RX = [None]*2056

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

	ser_MCU.sendall(str(TX).encode())
#	for data in TX:
#		ser_MCU.send(str(data).encode())
	

# From here, the code starts to count the error number

	loop_number = 0 # this number is in range of [0, test_round]
	address = 0  #output sequence

	
	err_sum = 0

	for i in range (2056):
		rx = ser_MCU.recv(1)
		RX[i] = int(rx)

	for j in range (2056):
		if (j != 0 and j%257 != 0):

			if(RX[j] != data_compare):

				err_number = RX[j] ^ data_compare
				err_number_binary = bin(err_number).count('1')

				err_sum = err_number_binary + err_sum

	print('The total number of generated errors is: ' + str(err_sum))



except KeyboardInterrupt:
	ser_MCU.close()
	print('Connection is closed!')
