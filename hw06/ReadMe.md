Trey Lewis      ECE 434

Homework 6 items:

	Project:
		I have added a project the the Project Page, and also put my name on a few projects that I am interested in doing that
                others have already suggested.

	Watch:
		1) National Instruments

		2) PREEMPT_RT is a real-time kernel patch that turns Linux into a real-time system. Useful when embedded projects need
		   a real-time operating system.

		3) Two different degrees of time-sensitive requirements. Tasks that have real-time requirements and those that have
		   non-time critical requirements.
 
		4) When the drivers are shared between real-time tasks and non-real-time tasks and try to isolate the two, they can 
		   misbehave.

		5) Julia calls it "the delta," I like to refer to it as latency. It is essentially the time between when an external
		   event occurs (a timer, I/O device, etc.) and when the relevant real-time task executes.

		6) A method to accurately and repeatedly measure the time difference between when a thread is supposed to wake up and
		   when it is actually woken up and running again. They are used to provide statistics on the latency of a system.

		7) The latency or "the delta" of a system with a non-real-time kernel (purple line) versus that with a real-time kernel
		   (green line).

		8) Dispatch Latency: The amount of time it takes between the hardware event actually firing and the thread scheduler
		   being told a particular thread needs to run.

		   Scheduling Latency: The amount of time it takes between the scheduler being told a task needs to be run to when the
		   CPU has been given the task to execute.
  
		9) A model showing a timeline of events and interrupts in a kernel.

		10) The interrupt handler is has already scheduled and is executing some other lower priority task.

		11) IRQ Threads are used to wake up the associated handler thread, so when the External Event is requested, it can be
		    scheduled immediately. 

========================
Professor Yoder's Comments

Score:  10/10

Try searching "linux mainline"