import serial
import time

#a = 1100
global i
i=0
ser = serial.Serial(
    port = '/dev/ttyAMA0',
    baudrate = 9600,
    parity = serial.PARITY_NONE,
    stopbits = serial.STOPBITS_ONE,
    bytesize = serial.EIGHTBITS,
    timeout = 1)

try:
     while i<10:
#        ser.write('00000'.encode())
#        ser.write('\t'.encode())
        
#        ser.write('\n'.encode())
        time.sleep(1)
        ser.write('01005'.encode())
#        ser.write('\n'.encode()*2)
#        time.sleep(1)
        i = i+1
        
#   while True:
#        rev = ser.readline()
#        print(rev.decode('utf-8'))
except KeyboardInterrupt:
    ser.close()
