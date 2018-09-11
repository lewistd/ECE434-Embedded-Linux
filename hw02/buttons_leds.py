import Adafruit_BBIO.GPIO as GPIO
#import time

led1 = "P9_11"
led2 = "P9_15"
led3 = "P9_14"
led4 = "P9_17"
button1 = "P9_42"
button2 = "P9_27"
button3 = "P9_23"
button4 = "P9_25"
#set the leds as outputs and buttons as inputs
GPIO.setup(led1, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)
GPIO.setup(led3, GPIO.OUT)
GPIO.setup(led4, GPIO.OUT)
GPIO.setup(button1, GPIO.IN)
GPIO.setup(button2, GPIO.IN)
GPIO.setup(button3, GPIO.IN)
GPIO.setup(button4, GPIO.IN)
#while button 1 is being pressed, turn on led 1 and check for exit case
def callback1(var): 
	while GPIO.input(button1):
		if GPIO.input(button2):
			GPIO.output(led1, GPIO.LOW)
			GPIO.cleanup()
			exit()
		GPIO.output(led1, GPIO.HIGH)
	GPIO.output(led1, GPIO.LOW)
#while button 2 is pressed, turn on led 2, turn off when released
def callback2(var):
	while GPIO.input(button2):
		GPIO.output(led2, GPIO.HIGH)
	GPIO.output(led2, GPIO.LOW)
def callback3(var):
	while GPIO.input(button3):
		GPIO.output(led3, GPIO.HIGH)
	GPIO.output(led3, GPIO.LOW)
def callback4(var):
	while GPIO.input(button4):
		GPIO.output(led4, GPIO.HIGH)
	GPIO.output(led4, GPIO.LOW)
#add each interrupt so they are listened for
GPIO.add_event_detect(button1, GPIO.RISING, callback=callback1, bouncetime=300)
GPIO.add_event_detect(button2, GPIO.RISING, callback=callback2, bouncetime=300)
GPIO.add_event_detect(button3, GPIO.RISING, callback=callback3, bouncetime=300)
GPIO.add_event_detect(button4, GPIO.RISING, callback=callback4, bouncetime=300)

while(1):
	pass
