Trey Lewis	ECE 434

Homework 3 items:

	TMP101:
		-The two TMP101 sensors are both wired up correctly.
		-My shell script getTemp.sh reads both sensors, converts each temperature to Fahrenheit, and prints each result to the console.
		-Run the script with './getTemp.sh' (if for some reason it doesn't work, run 'chmod +x getTemp.sh' first then try './getTemp.sh')
		-The addresses of my sensors were 0x48 and 0x4a on bus 2

	Etch-a-sketch & Rotary Encoders:
		-The etch-a-sketch is successfully interfaced with the 8x8 led matrix and rotary encoders.
		-Use the rotary encoders to draw, one does up and down movement, the other does left and right movement. The feeling is very responsive.
		-The etch-a-sketch also wraps around to the other side of the display in any direction.
		-To run the program, input the command 'python etch.py' (ctrl+C to quit the program)
		-Display is left where last marked when quitting and resets when run again.
		-Instructions are printed out when the program starts.
		-Note: I had to run 'config-pin P8_41 qep' and 'config-pin P8_42 qep' to get one of the encoders to work. The other pins to run this on would be P8_33 and P8_35.
