Trey Lewis      ECE 434

Homework 2 items:

        Buttons and LEDs:
		This program is fully functional.
                Wired circuit with 4 pushbuttons and 4 LEDs. My program is written in Python and lights up a LED when the      
                corresponding button is pressed. To run the program, type "python buttons_leds.py" in the command line while
		in the folder containing the file. To exit, press buttons 1 and 2 simultaneously. A list of the pin locations
		is below and can also be easily seen in the code.
		
		Button 1 - P9_42 | gpio7	=	LED 1 - P9_11 | gpio30
		Button 2 - P9_27 | gpio115	=	LED 2 - P9_15 | gpio48
		Button 3 - P9_23 | gpio49	=	LED 3 - P9_14 | gpio50
		Button 4 - P9_25 | gpio117	=	LED 4 - P9_17 | gpio5

		Button clear - P9_26 | gpio14 (no LED for this one, it's used in the Etch-A-Sketch program)

	Measuring a gpio pin on an Oscilloscope:

		The results for this section are in the Results.pdf file.

	Etch-a-sketch:
		
		The update to my program is complete and fully functional. Code to control the cursor with arrow keys has been commented out, and
		the only way to control it is with pushbuttons on the pins specified above. Use of the 'p', 'c', and 'backspace'
		keys still work. To run the program, type "python etch.py" in the command line while in the folder containing the
		file. Instructions for the program are printed at the start of the program. 

	Extras (optional?):

		There is a button to clear and reset the display.
		Pressing 'c' will also clear and reset the display.
		Pressing 'p' will pick up the pen so that the trace is no longer shown. Pressing 'p' again will put the pen back down.
		Modify togglegpio.c: Run with "./togglegpio" to see further instructions.
				     takes the gpio number and takes on and off times separately (in us). There is an interrupt handler
				     that detects ctrl+C and closes properly. The highest frequency I found with the function was 3.625 khz.
		Modify gpioThru.c: Run with "./gpioThru" to see further instructions.
				        set to count only releases, count implemented (but still buggy).
					Code added to duplicate the input gpio's value to output on gpio30

========================
Professor Yoder's Comments

Looks very good.  Nice and complete.  Good tables.

Score:10/10
