import RPi.GPIO as gpio
import time

error_output_pin = 36

chain_output_pin = 35

chain_number = 6

error_number = 5

def setup():
    gpio.setmode(gpio.BOARD)
    gpio.setup(error_output_pin, gpio.OUT)
    gpio.output(error_output_pin, gpio.LOW)
    gpio.setup(chain_output_pin, gpio.OUT)
    gpio.output(chain_output_pin, gpio.LOW)
    
if __name__ == "__main__":
    setup()
    try:
#        for a in range (0, 10):
        while True:
            for i in range (0,chain_number):
                gpio.output(chain_output_pin, gpio.HIGH)
                gpio.output(chain_output_pin, gpio.LOW)
#            time.sleep(1)
#            time.sleep(2)
            for j in range (0,error_number):
                gpio.output(error_output_pin, gpio.HIGH)
                gpio.output(error_output_pin, gpio.LOW)
            time.sleep(1)
            
        gpio.cleanup()
        
    except KeyboardInterrupt:
        gpio.cleanup()