#include <xc.h>
#include <pic16f886.h>
#include "conbits.h"


 //Interrupt Service Routine - ISR
void __interruptISR()
{
   if (TMR1IF)// Timer 1 Flag bit
   {
            RC3=1;
            TMR1IF=0;
            TMR1 = 64535;
            timer_overflow_counter++;
            if(timer_overflow_counter==timer_overflows)
            {
                TMR1ON = 0;
                timer_overflow_counter=0;
                RC3=~RC3;
                Timer_set_ms_interrupt(1000);
            }
            
   }
}

void main(void) {
    SCS=1;
    TRISC3=0;
    RC3=0;
    __delay_ms(1000);
    Timer_set_ms_interrupt(1000);
    while(1)
    {
    }
}
