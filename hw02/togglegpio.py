# Toggle gpio pin with Python
import Adafruit_BBIO.GPIO as GPIO
import time

gpio = raw_input("Enter the GPIO pin (ex. PX_XX): ")
period = input ("Enter the period (in seconds): ")

GPIO.setup(gpio, GPIO.OUT)

while True:
    GPIO.output(gpio, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(gpio, GPIO.LOW)
    time.sleep(0.5)

