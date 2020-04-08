import RPi.GPIO as GPIO

PulseInput = 11
#Rpin = 12
#Gpin = 13
global counter
counter = 0

def setup():
    GPIO.setmode(GPIO.BOARD)
    #GPIO.setup(Rpin, GPIO.OUT)
    #GPIO.setup(Gpin, GPIO.OUT)
    GPIO.setup(PulseInput, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
    #the pull up/down supply that voltage so that the gpio will have a defined value UNTIL overridden by a stronger force.
    #you should set a pull down (to 0) when you expect the stronger force to pull it up to 1.
    #GPIO.add_event_detect(PulseInput, GPIO.RISING, callback=detect, bouncetime=200)
    GPIO.add_event_detect(PulseInput, GPIO.RISING, callback=detect)

'''def Led(x):
    if x == 0:
        #GPIO.output(Rpin, 1)
        GPIO.output(Gpin, 0)
    if x == 1:
        #PIO.output(Rpin, 0)
        GPIO.output(Gpin, 1)'''
        
def Count(x):

    global counter
    #counter = counter + 1
    counter += 1
    #print("The pulse number is: {0}".format(counter))
    
    #    if x == 1:
    print("There is the ", counter, " pulse received!")
    print()
	
def detect(chnIn):
    Count(GPIO.input(PulseInput))
 #   Led(GPIO.input(PulseInput))
    
def loop():
    while True:
        pass
        #if counter != 0 :            
            #pass
            #print("The pulse number is: {0}".format(counter))

def destroy():
    print("The pulse number is: {0}".format(counter))
    #GPIO.output(Gpin, GPIO.LOW)
    GPIO.cleanup()
    
if __name__ == '__main__':
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()

     