#include <stdio.h>
#include <stdlib.h>
#include <sys/mman.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <signal.h>    // Defines signal-handling functions (i.e. trap Ctrl-C)
#include "beaglebone_gpio.h"

/****************************************************************
 * Global variables
 ****************************************************************/
int keepgoing = 1;    // Set to 0 when ctrl-c is pressed

/****************************************************************
 * signal_handler
 ****************************************************************/
void signal_handler(int sig);
// Callback called when SIGINT is sent to the process (Ctrl-C)
void signal_handler(int sig)
{
	printf( "\nCtrl-C pressed, cleaning up and exiting...\n" );
	keepgoing = 0;
}

int main(int argc, char *argv[]) {
    volatile void *gpio_addr;
    volatile unsigned int *gpio_oe_addr;
    volatile unsigned int *gpio_setdataout_addr;
    volatile unsigned int *gpio_cleardataout_addr;
    unsigned int reg;

    // Set the signal callback for Ctrl-C
	signal(SIGINT, signal_handler);

    int fd = open("/dev/mem", O_RDWR);

    gpio_addr = mmap(0, GPIO1_SIZE, PROT_READ | PROT_WRITE, MAP_SHARED, fd, GPIO1_START_ADDR);

    gpio_oe_addr           = gpio_addr + GPIO_OE;
    gpio_setdataout_addr   = gpio_addr + GPIO_SETDATAOUT;
    gpio_cleardataout_addr = gpio_addr + GPIO_CLEARDATAOUT;

    if(gpio_addr == MAP_FAILED) {
        printf("Unable to map GPIO\n");
        exit(1);
    }

    // Set GPIO50 to be an output pin
    reg = *gpio_oe_addr;
    reg &= ~LED_1;       // Set USR3 bit to 0
    *gpio_oe_addr = reg;

    printf("Start toggling gpio1[18]\n");
    while(keepgoing) {
        // printf("ON\n");
        *gpio_setdataout_addr = LED_1;
        usleep(5000);
        // printf("OFF\n");
        *gpio_cleardataout_addr = LED_1;
        usleep(5000);
    }
    // cleanup
    munmap((void *)gpio_addr, GPIO1_SIZE);
    close(fd);
    return 0;
}
