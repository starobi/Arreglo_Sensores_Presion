 /*
 * File:   4_Timer_test.c
 * Author: staro
 *
 * Created on 14. März 2022, 21:22
 */


#include <xc.h>
#include <pic16f886.h>
#include "conbits.h"


// Interrupt Service Routine - ISR
//void __interruptISR()
//{
//   if (TMR1IF)// Timer 1 Flag bit
//   {
//       count++;
//       if(count==5000)
//       {
//           TMR1ON = 0;
//        //Toggle RC3
//           RC2 =1;
//       }
//       //Timer_Interrupt_Hanlde();
//   }
//}

void main(void) {
    SCS=1;
    TRISC3=0;
    RC3=0;
    Timer_set_ms_polling(1000);
    while(1)
    {
        if(TMR1IF)
        {
            TMR1 = 64535;
            TMR1IF=0;
            timer_overflow_counter++;
            if(timer_overflow_counter==timer_overflows)
            {
                timer_overflow_counter=0;
                RC3=~RC3;
            }
        }
    }
}
