Trey Lewis      ECE 434

Homework 4 items:

	Memory Map:

		-See the MemoryMap pdf file included in this hw04 directory for my version of the BeagleBone memory map.
		-I also printed out the Memory Map and GPIO register Table 25-5 from the AM335x TRM.

	GPIO via mmap:
		
		-All necessary files for this section of the homework are located in the 'mmap' directory.

		Read Switches & Control LEDs:

			I was able to successfully map two buttons from separate GPIO ports (port 0 & port 1) to two LEDs (also on separate ports) by reading and writing GPIO ports via memory map.
			-To run this program, do a 'make' while in the 'mmap' directory, run the setup script (may need to do it twice), and then run the gpioThru executable. 
			
		Toggle GPIO fast:
			The shortest period I was able to obtain by toggling the GPIO port via mmap was: 142us
			-Toggling GPIO via mmap was the fastest among all the methods I have tested, barely eclipsing GPIO via Python (for complete test results, refer to hw02).
			-Here are the shortest periods for each method I have tested.
				-mmap:		142 us
				-Python:	168.6 us
				-C:		276.4 us
				-Shell:		35.4 ms

	Extras:
		
		I was unable to get accurate readings from running the setup script then gpioThru. The program seemed to often get stuck in a state where it wasn't doing anything, but I also could not
		exit it. When I would input Ctrl+C to exit the program, I would get the exit prompt, but I would still be stuck in the program with nothing happening. Not sure why this was happening 
		or what could have caused it. The times I could get the program to run I only saw voltage changes in one of the pins change voltage level on the oscope, so I couldn't get a reading for
		the delay time. I didn't make changes to the gpioThru.c file, and ran the setup shell script, so I'm not sure what was causing the issues. 

		-However, I was able to get a delay time using the modified gpioThru that I used for the buttons. Using this, I measured a delay time of 400ns. I will hopefully be able to include an
		image in the hw04 folder. 
	
	2.4" TFT LCD Display:

		-The LCD is wired correctly and functioning as it should.
		-all necessary files are in the 'movies' subdirectory of the 'hw04' directory
		-To display Boris on the LCD, run the command 'sudo fbi -noverbose -T 1 -a boris.png'
		-To display Boris rotated 90 degreen, replace 'boris.png' with 'boris-rotated.png' in the command above.
		-To play the movie RedsNightmare.mpg, run the play_movie script (./play_movie.sh). Run chmod on it if for some reason the script doesn't work immediately.	
		-To play the movie but rotated, run the play_movie_rotated script.
		-To view my image with text on it, run the image_text script.
		-I will include pictures I took of the LCD working on my BeagleBone

========================
Professor Yoder's Comments

Looks very good.  Nice and complete.
I don't know why the gpioThru.c isn't working.

Score:  10/10