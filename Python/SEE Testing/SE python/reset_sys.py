import RPi.GPIO as GPIO
import time

def reset(pin):
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(pin, GPIO.LOW)
    time.sleep(1)
    return

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT, initial=GPIO.LOW)

rst = input("Do you want to reset system?\n")
while True:
    if rst == "y":
        reset(7)
        GPIO.output(7, GPIO.LOW)
        rst = input("Do you want to reset system?\n")
    elif rst == "n":
        GPIO.output(7, GPIO.LOW)
        break
    else:
        GPIO.output(7, GPIO.LOW)
        rst = input("Do you want to reset system?\n")

GPIO.cleanup()
exit

