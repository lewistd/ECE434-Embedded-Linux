# Toggle gpio pin with Python
import Adafruit_BBIO.GPIO as GPIO
import time

gpio = raw_input("Enter the GPIO pin (ex. PX_XX): ")
period = input ("Enter the period (in seconds): ")

half_period = period/2
GPIO.setup(str(gpio), GPIO.OUT)

while True:
    GPIO.output(str(gpio), GPIO.HIGH)
    time.sleep(half_period)
    GPIO.output(str(gpio), GPIO.LOW)
    time.sleep(half_period)

