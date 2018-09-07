#!/usr/bin/env python

import curses

#print out the instructions
print "\nINSTRUCTIONS:"
print "\nUp arrow moves up 1 space"
print "Down arrow moves down 1 space"
print "Right arrow moves right 1 space"
print "Left arrow moves left 1 space"
print "Press 'p' to pick up the pen"
print "Press 'c' to clear screen and return to starting position"
print "Press backspace to exit the program"
raw_input("\nPress enter to begin")
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
#mark starting position
stdscr.addch('x')
stdscr.move(x,x)

while True:
    #listen for keypress
    ch = stdscr.getch()
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
        x = 0
        y = 0
        stdscr.move(y,x)
        if pen_down:
            stdscr.addstr('x')
            stdscr.move(y,x)

    if ch == ord('p'):
        #pick up/put down pen
        pen_down = not pen_down

    if ch == curses.KEY_BACKSPACE:
        #close windown and return to terminal
        curses.endwin()
        exit()

