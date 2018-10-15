Trey Lewis      ECE 434

Homework 8 items:

        PREEMPT_RT:

		I was able to successfully generate png files for each of the two cases, one with no load and one with a heavy load. 
		In the png files there are two plots, One generated from the RT kernel and one from the non-RT kernel. The file with no
		load is named 'out-noload.png'. You can view it with any program for viewing images on the host computer. In that plot,
		the RT kernel runtime is only slightly shorter than the non-rt kernel. With no load, there is not much for the rt
		kernel to do to optimize the runtime, so the two kernels have a very similar runtime. However, in the case with a heavy
		load, the rt kernel had a significantly shorter runtime than the non-rt kernel. Under the heavy load, the rt kernel is
		able to preempt the task to make it a higher priority, and thus finish in a time much closer to the case with no load. 
		This can be seen in the file 'out-heavyload.png' Meanwhile, the non-rt kernel cannot do this, so the task is not 
		preempted while the background load is running, which causes the runtime to be much greater. These outputs are what I 
		expected and show the benefits of using an rt kernel for timing-critical tasks.
