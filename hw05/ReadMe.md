Trey Lewis      ECE 434

Homework 5 items:

	Project:

		I have added a project the the Project Page, and also put my name on a few projects that I am interested in doing that
		others have already suggested.

	Make:

		I have completed the 'make' exercise on the wiki and my make file and all necessary files for it are located in the
		'make' folder of the 'hw05' directory. It functions just as is stated in the wiki. The three commands you can use while
		in the 'make' folder are 'make', 'make clean', and 'make test'. To run the sample program, run 'make' then './app.arm'.

	Installing the Kernel Source:

		I was able to successfully download and build the 4.x Kernel on my host machine then install and run the kernel on my bone.

	Cross-Compiling:

		I was able to successfully complete the exercise and cross-compile the "Hello World" program on my bone. I will include
		screen captures of the ouput of the program for the host and the bone in the 'cross-compiling' directory along with a.out.

	Kernel Modules:

		Part 1:
			I followed Part 1 of the blog and was able to insert and remove the LKM and see the output printed to the console.
			I have included the necessary files for building the module along with the module itself in the 'kernel_mods1' 
			folder. To build the LKM, simply run make. Then the hello.ko kernel mod can be inserted or removed. I have included
			a screen capture of the output to the terminal.

		Part 2:
			I followed Part 2 of the blog and was able to use the character device module to send data from the user space to
			the kernel space, and back to the user space. I have included the necessary files for building and running the module
			in the 'kernel_mods2' folder. To build the LKM, run make. Insert the ebbchar.ko kernel mod then run the user program
			with './test' to send data to the kernel and receive it back. Then remove the mod. I have included a screen capture
			of the output to the terminal from running the mod and user program.

		Part 3:
			I followed Part 3 of the blog and was able to change the c file to copy P9_15 to P9_16. When I ran the module, the
			led on P9_16 was successfully inverted with each button press. I have included the necessary files for building and
			running the module in the 'kernel_mods3' folder as well as a screen capture of the kernel log while running the mod.
			To build the LKM, run make. Then insert the mod 'gpio_test.ko'. The led will now invert on the button press. Remove
			the mod when finished. The module also displays other information, like how many times the button was pressed, when
			the mod is closed.


========================
Professor Yoder's Comments

Looks very good.  Nice and complete.
Which version of the kernel are you running now?

--- (Trey)  I am running kernel version 4.9.119

my output from 'uname -r'  4.9.119-bone11

Score:  10/10
