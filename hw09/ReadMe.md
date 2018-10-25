Trey Lewis      ECE 434

Homework 9 items:
	
	There is a table with a summary of the results of each section titled 'results.png' in this folder. Look there for all of the data for this homework assignment.

        Blinking an LED:

		The highest frequency I was able to toggle the output at was 12.5 MHz. The jitter was very noticeable throughout the entire waveform. For the most part, the waveform seemed to be stable.

	PWM Generator:

		I was able to get the frequency of the waveform to be at exactly 50 MHz by adding in an extra delay cycle. So, this resulted in a standard deviation of 0. I did not notice any jitter in 
		this waveform, and althought it wasn't a square wave, the waveform was stable as it's frequency was very consistent.

	Controlling the PWM Frequency:

		In this part, I had the code for 4 channels, but only hooked up 2 to the oscilloscope. The highest frequency I observed was 327 kHz. The waveform produced was very stable and had no
		noticeable jitter. 

	Loop Unrolling for Better Performance:

		In this section, I implemented loop unrolling to improve the performance of the program. As a result, the new highest frequency I observed was 1.67 MHz, which was a 5.1x speedup from the
		result of the previous section (5.4 - Controlling the PWM Frequency) which had a frequency of 327 kHz. The waveform produced had very slight jitter, I was able to barely notice it moving
		back and forth. However, the waveform was still stable.

	Reading an Input at Regular Intervals:

		I have included two scope captures in this section, one that shows copying the input to the output multiple times, and the other zoomed in to see the timing of the copy. Using this
		second scope capture, I measured the time to copy the input to the output to be 27.00 ns.

	Analog Wave Generator (optional):

		I did not complete this optional section.


