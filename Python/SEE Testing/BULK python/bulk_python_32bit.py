#! /usr/bin/python
import serial
import time
import threading
import random
from queue import Queue

# 0 -- 100MHZ
# 1 -- 10MHz
# 2 -- 1MHz
# 3 -- 100kHz
clk_ctrl = 2
# 0 -- all 0
# 1 -- all 1
# 2 -- half-half
# 3 -- self check
dat_ctrl1 = 2
# 0 -- all 0
# 1 -- all 1
# 2 -- half-half
# 3 -- self check
dat_ctrl2 = 2

def transmit():
    ser.flushInput()
    num=[]
    num.append(0)
    num.append(dat_ctrl2+dat_ctrl1*4 + clk_ctrl * 16)#for the test
    print(num)

    i = 0
    while True:
            if i<2:
                dout = num[i]
                tx = (dout).to_bytes(1, byteorder='big')
                ser.write(tx)
                i += 1
                time.sleep(0.001)



def receive():
    ser.flushOutput()
    cnt = 0
    cnt2 = 0
    output1 = []
    output2 = []
    data = []
    freq_real = 0
    
    while True:
        if ser.inWaiting() != 0:
            if cnt < 12:
                dfile = open("/home/pi/Desktop/%s.txt" %(StartTime),"a")
                rx = ser.read(1)         #32bit
                output2.append(int.from_bytes(rx, byteorder='big'))
                #print(output)
                cnt += 1
               # else:
                #    time.sleep(0.01)
                #    cnt = 0
                #    cnt2 = 0
                #    output = []
                #    data = []
                #    freq = []
            else:
                if cnt2 == 0:
                    output1 = output2
                    output2 = []
                    cnt2 += 1
                    cnt = 0
                else:
                    for i in range(len(output1)):
                        data.append(output2[i] - output1[i])
                    output1 = output2
                    dfile.write(" %s \r\n" %(data[0:12]))
                    print(data[0:12])
                    output2 = []
                    data = []
                    cnt = 0
                    dfile.close()
                
def stop(q):
    q.put(input("Do you want to quit the program? (y/n)\n"))


if __name__=='__main__':
#setup the serial port
    ser = serial.Serial('/dev/ttyAMA0', 115200, parity=serial.PARITY_EVEN, stopbits=serial.STOPBITS_ONE)

    #show the local time
    StartTime = time.strftime("%Y_%m_%d_%I:%M:%S", time.gmtime())
    print("The beginning time: ", StartTime)

    #creat a file to save the data
    dfile = open("/home/pi/Desktop/%s.txt" %(StartTime),"w")

    #check whether serial connect
    if ser.isOpen() == False:
        ser.open()
        

    result = 0
    q = Queue()
    t = threading.Thread(target=transmit)
    r = threading.Thread(target=receive)
    s = threading.Thread(target=stop, args=(q,))
    r.setDaemon(True)
    t.setDaemon(True)
    t.start()
    r.start()
    s.start()
    

    result = q.get()
    if result == "y":
        tx_stp = b'\xff'
        ser.write(tx_stp)
        print(tx_stp)
        time.sleep(1)
        print("The work is done")
        ser.close()
        dfile.close()
    else:
        r.join()
        print("The work is done")
        ser.close()
        dfile.close()

   
    