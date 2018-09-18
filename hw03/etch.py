#!/usr/bin/env python

import smbus
import time
from Adafruit_BBIO.Encoder import RotaryEncoder, eQEP2, eQEP1
import Adafruit_BBIO.GPIO as GPIO
bus = smbus.SMBus(2)
matrix = 0x70
myEncoder1 = RotaryEncoder(eQEP1)
myEncoder1.setAbsolute()
myEncoder1.enable()
myEncoder2 = RotaryEncoder(eQEP2)
myEncoder2.setAbsolute()
myEncoder2.enable()

y = 0

bus.write_byte_data(matrix, 0x21, 0)   # Start oscillator (p10)
bus.write_byte_data(matrix, 0x81, 0)   # Disp on, blink off (p11)
bus.write_byte_data(matrix, 0xe7, 0)   # Full brightness (page 15)

display = [0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]

bus.write_i2c_block_data(matrix, 0, display)

#print out the instructions

while True:
	print("Encoder 1: " + str(myEncoder1.position))
	print("Encoder 2: " + str(myEncoder2.position))

	if(myEncoder1.position > 0): #move right
		display[y] = display[y] * 2 + 1
	elif(myEncoder1.position < 0): #move left
		y = 0
	elif(myEncoder2.position > 0): #move down
		if(y+2 < 16):
			y += 2
			display[y] = display[y] * 2 + 1
	elif(myEncoder2.position < 0): #move up
		y = 0

	bus.write_i2c_block_data(matrix, 0, display)
	myEncoder1.zero()
	myEncoder2.zero()

	time.sleep(0.1)
