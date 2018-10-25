#include <stdint.h>
#include <pru_cfg.h>
#include "resource_table_empty.h"

#define GPIO3 0x481AE000
#define GPIO1 0x4804C000
#define GPIO_CLEARDATAOUT 0x190
#define GPIO_SETDATAOUT 0x194
#define USR0 (1<<21)
#define USR1 (1<<22)
#define USR2 (1<<23)
#define USR3 (1<<24)
#define LED3 (1<<19) //P9_27
#define LED1 (1<<28) //P9_12
unsigned int volatile * const GPIO3_CLEAR = (unsigned int *) (GPIO3 + GPIO_CLEARDATAOUT);
unsigned int volatile * const GPIO3_SET   = (unsigned int *) (GPIO3 + GPIO_SETDATAOUT);

volatile register unsigned int __R30;
volatile register unsigned int __R31;

void main(void) {
	int i;

	/* Clear SYSCFG[STANDBY_INIT] to enable OCP master port */
	CT_CFG.SYSCFG_bit.STANDBY_INIT = 0;

	while(1) { //for(i=0; i<5; i++) {
		*GPIO3_SET = LED3;      // The the USR3 LED on
//		__delay_cycles(500000000/5);    // Wait 1/2 second
		__delay_cycles(0);
		*GPIO3_CLEAR = LED3;
//		 __delay_cycles(500000000/5);
		__delay_cycles(0);
	}
	__halt();
}
