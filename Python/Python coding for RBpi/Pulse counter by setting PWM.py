import RPi.GPIO as g
import time

print ("Current GPIO version : " + g.VERSION)
g.setmode(g.BOARD)

receiverPin = 11
pulseGeneratorPin = 12
global counter
counter = 0
frequency = 10000
dutyCycle = 50 #change the pulse width
duration = 1

g.setup(receiverPin, g.IN, pull_up_down=g.PUD_DOWN)
g.setup(pulseGeneratorPin, g.OUT)

p = g.PWM(pulseGeneratorPin, frequency)
p.start(dutyCycle)

def Count(x):
    global counter
    counter = counter + 1 #or: counter += 1

print("Testing Parameters : Frequency: "+str(frequency) +"; DutyCycle: "+str(dutyCycle) +"; Duration: "+str(duration) +" seconds")

g.add_event_detect(receiverPin, g.RISING, callback=Count)
time.sleep(duration) #it pauses the Python code for "duration" time.
g.remove_event_detect(receiverPin)
      
print("The total pulses are:  "+str(counter))
print("Pulses per second:  "+str(counter/duration))
print("Test End")
      
g.cleanup()
      