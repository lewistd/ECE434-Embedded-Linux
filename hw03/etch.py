#!/usr/bin/env python

import smbus
import time
from Adafruit_BBIO.Encoder import RotaryEncoder, eQEP2, eQEP1
import Adafruit_BBIO.GPIO as GPIO
bus = smbus.SMBus(2) # bus select
matrix = 0x70 # matrix addr

# setup rotary encoders
myEncoder1 = RotaryEncoder(eQEP1)
myEncoder1.setAbsolute()
myEncoder1.enable()
myEncoder2 = RotaryEncoder(eQEP2)
myEncoder2.setAbsolute()
myEncoder2.enable()

y = 0
x = 0

bus.write_byte_data(matrix, 0x21, 0)   # Start oscillator (p10)
bus.write_byte_data(matrix, 0x81, 0)   # Disp on, blink off (p11)
bus.write_byte_data(matrix, 0xe7, 0)   # Full brightness (page 15)

# initially have top left led on in the led matrix
display = [0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]

# write the matrix to the led display
bus.write_i2c_block_data(matrix, 0, display)

#print out the instructions
print "\nINSTRUCTIONS:\n"
print "Use the knobs to control the etch-a-sketch on the 8x8 biLED matrix"
print "Quit with ctrl+C"

while True:
#	print("Encoder 1: " + str(myEncoder1.position))
#	print("Encoder 2: " + str(myEncoder2.position))

	if(myEncoder1.position > 0): #move right
		x += 1
		if(x < 8):
			temp = display[y]
			display[y] = 1<<x
			display[y] = display[y] | temp
#		handle for wraparound moving right
		elif(x >= 8):
			x = 0
			temp = display[y]
                        display[y] = 1<<x
			display[y] = display[y] | temp
	elif(myEncoder1.position < 0): #move left
		x -= 1
		if(x >= 0):
			temp = display[y]
			display[y] = 1<<x
			display[y] = display[y] | temp
#		handle for wraparound moving left
		elif(x < 0):
			x = 7
			temp = display[y]
			display[y] = 1<<x
			display[y] = display[y] | temp
	elif(myEncoder2.position > 0): #move down
		y += 2
		if(y < 16):
			temp = display[y]
			display[y] = 1<<x
			display[y] = display[y] | temp
#		handle for wraparound moving down
		elif(y >= 16):
			y = 0
			temp = display[y]
                        display[y] = 1<<x
                        display[y] = display[y] | temp
	elif(myEncoder2.position < 0): #move up
		y -= 2
		if(y >= 0):
			temp = display[y]
                        display[y] = 1<<x
                        display[y] = display[y] | temp
#		handle for wraparound moving up
		elif(y < 0):
			y = 14
			temp = display[y]
                        display[y] = 1<<x
                        display[y] = display[y] | temp
	bus.write_i2c_block_data(matrix, 0, display)
	myEncoder1.zero()
	myEncoder2.zero()

	time.sleep(0.1)
