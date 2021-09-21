/*
 * File:   Main.c
 * Author: staro
 *
 * Created on 12. April 2021, 16:00
 */


#include <xc.h>
#include <pic16f886.h>
#include "conbits.h"

void main(void) {
    TRISC=0x00;
    while(1)
    {
        PORTC=0x00;
         __delay_ms(1000);
        PORTC=(1<<1);
        __delay_ms(1000);
        
    }
    
    
    return;
}
