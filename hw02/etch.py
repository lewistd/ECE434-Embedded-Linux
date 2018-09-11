#!/usr/bin/env python

import curses
import Adafruit_BBIO.GPIO as GPIO

#print out the instructions
print "\nINSTRUCTIONS:"
print "\nUp arrow moves up 1 space"
print "Down arrow moves down 1 space"
print "Right arrow moves right 1 space"
print "Left arrow moves left 1 space"
print "Press 'p' to pick up the pen"
print "Press 'c' to clear screen and return to starting position"
print "Press backspace to exit the program"
print "\nThe pen can also be moved with the buttons attached to the Beaglebone"
raw_input("\nPress enter to begin: ")
#initialize the screen
stdscr = curses.initscr()
#don't echo keypresses
curses.noecho()
#allow alternate keys to be used
stdscr.keypad(True)

x = 0
y = 0
#this will determine whether to write out to screen
pen_down = True

button1 = "P9_42"
button2 = "P9_27"
button3 = "P9_23"
button4 = "P9_25"
#set the buttons as inputs
GPIO.setup(button1, GPIO.IN)
GPIO.setup(button2, GPIO.IN)
GPIO.setup(button3, GPIO.IN)
GPIO.setup(button4, GPIO.IN)
#when button 1 is pressed, mark an 'x' if necessary and move one space right
def callback1(var):
	y, x = stdscr.getyx()
        stdscr.move(y,x+1)
        if pen_down:
            stdscr.addstr('x')
            stdscr.move(y,x+1)
	stdscr.refresh()
#while button 2 is pressed, turn on led 2, turn off when released
def callback2(var):
	y, x = stdscr.getyx()
	if x != 0:
            stdscr.move(y,x-1)
            if pen_down:
                stdscr.addstr('x')
                stdscr.move(y,x-1)
	stdscr.refresh()
def callback3(var):
	y, x = stdscr.getyx()
        stdscr.move(y+1,x)
        if pen_down:
            stdscr.addstr('x')
            stdscr.move(y+1,x)
	stdscr.refresh()
def callback4(var):
	y, x = stdscr.getyx()
        if y != 0:
            stdscr.move(y-1,x)
            if pen_down:
                stdscr.addstr('x')
                stdscr.move(y-1,x)
	stdscr.refresh()

#add each interrupt so they are listened for
GPIO.add_event_detect(button1, GPIO.RISING, callback=callback1, bouncetime=300)
GPIO.add_event_detect(button2, GPIO.RISING, callback=callback2, bouncetime=300)
GPIO.add_event_detect(button3, GPIO.RISING, callback=callback3, bouncetime=300)
GPIO.add_event_detect(button4, GPIO.RISING, callback=callback4, bouncetime=300)

#mark starting position
stdscr.addch('x')
stdscr.move(0,0)
stdscr.refresh()

while True:
    #listen for keypress
    ch = stdscr.getch()
    #get the yx location of the cursor
    y, x = stdscr.getyx()
    #based on the key that's pressed move, clear, or exit
    if ch == curses.KEY_DOWN:
        y = y+1
        stdscr.move(y,x)
        if pen_down:
            stdscr.addstr('x')
            stdscr.move(y,x)

    if ch == curses.KEY_UP:
        if y != 0:
            y = y-1
            stdscr.move(y,x)
            if pen_down:
                stdscr.addstr('x')
                stdscr.move(y,x)

    if ch == curses.KEY_RIGHT:
        x = x+1
        stdscr.move(y,x)
        if pen_down:
            stdscr.addstr('x')
            stdscr.move(y,x)

    if ch == curses.KEY_LEFT:
        if x != 0:
            x = x-1
            stdscr.move(y,x)
            if pen_down:
                stdscr.addstr('x')
                stdscr.move(y,x)

    if ch == ord('c'):
        #clear the screen and return to start position
        stdscr.clear()
        stdscr.move(0,0)
        if pen_down:
            stdscr.addstr('x')
            stdscr.move(0,0)

    if ch == ord('p'):
        #pick up/put down pen
        pen_down = not pen_down

    if ch == curses.KEY_BACKSPACE:
        #close windown and return to terminal
        curses.endwin()
        exit()

