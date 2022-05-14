/*
 * File:   Timer.c
 * Author: staro
 *
 * Created on 14. März 2022, 14:51
 */

#include "Timer.h"

uint16_t timer_overflows=0;
uint16_t timer_overflow_counter=0;

void Timer_set_ms_polling(uint16_t time)
{
   // -- [[ Configure Timer1 To Operate In Timer Mode&nbsp; ]] --
  //Set number of overflows
  timer_overflows=time;
  // Preload The Value Which We've Calculated To The TMR1 16-Bit Register!
  TMR1 = 64535;
  // Choose Microcontroller Clock
  TMR1CS = 0;
  // Choose the desired prescaler ratio (1:1)
  T1CKPS0 = 0;
  T1CKPS1 = 0;
  // -- [[ Interrupts Configurations ]] --
  TMR1IE = 0; // Timer1 Interrupt Enable Bit
  TMR1IF = 0; // Clear The Interrupt Flag Bit
  timer_overflow_counter=0; //Clear overflow Counter
  PEIE = 0;   // Peripherals Interrupts Enable Bit
  GIE = 0;    // Global Interrupts Enable Bit
  // Switch ON Timer1 Module!
  TMR1ON = 1;
}
void Timer_set_ms_interrupt(uint16_t time)
{
   // -- [[ Configure Timer1 To Operate In Timer Mode&nbsp; ]] --
  //Set number of overflows
  timer_overflows=time;
  timer_overflow_counter=0; //Clear overflow Counter
  // Preload The Value Which We've Calculated To The TMR1 16-Bit Register!
  TMR1 = 64535;
  // Choose Microcontroller Clock
  TMR1CS = 0;
  // Choose the desired prescaler ratio (1:1)
  T1CKPS0 = 0;
  T1CKPS1 = 0;
  // -- [[ Interrupts Configurations ]] --
  TMR1IE = 1; // Timer1 Interrupt Enable Bit
  TMR1IF = 0; // Clear The Interrupt Flag Bit
  
  PEIE = 1;   // Peripherals Interrupts Enable Bit
  GIE = 1;    // Global Interrupts Enable Bit
  
  // Switch ON Timer1 Module!
  TMR1ON = 1;
}

void Timer_Interrupt_Hanlde(void)
{
      TMR1IF = 0; // Clear The Flag Bit  
      timer_overflow_counter++;
      if(timer_overflow_counter==timer_overflows)
      {
        // Event2 = Toggle LED
        TMR1ON = 0;
        //Toggle RC3
        RC2 = ~RC2;
        // Clear The Global Counter
        timer_overflow_counter = 0;
        //Timer_set_ms(1000);
      }
      
}
