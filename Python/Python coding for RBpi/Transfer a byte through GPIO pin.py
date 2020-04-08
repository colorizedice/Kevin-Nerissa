import RPi.GPIO as gpio
import time

data_output_pin = 36

Data = [0, 0, 1, 0, 0, 0, 1, 1] #the first three digits stand for the number of chains, the last five digits stand for the number of errors

Start_bit = [1, 1]
Stop_bit = [0, 0]

def setup():
    gpio.setmode(gpio.BOARD)
    gpio.setup(data_output_pin, gpio.OUT)
    gpio.output(data_output_pin, gpio.LOW)
    
def Transfer_data():
    for bit1 in Start_bit:
        gpio.output(data_output_pin, bit1)
        time.sleep(0.01)
#        print(bit1)
    
    time.sleep(0.005)
    
    for bit2 in Data:
        gpio.output(data_output_pin, bit2)
        time.sleep(0.01)
#        print(bit2)
        
    time.sleep(0.005)
    
    for bit3 in Stop_bit:
        gpio.output(data_output_pin, bit3)
        time.sleep(0.01)
#        print(bit3)
        
#    time.sleep(2)
        
if __name__ =='__main__':
    
    setup()
    
    try:
#        while True:
        Transfer_data()
        gpio.cleanup()
    except KeyboardInterrupt:
        gpio.cleanup()
        


    