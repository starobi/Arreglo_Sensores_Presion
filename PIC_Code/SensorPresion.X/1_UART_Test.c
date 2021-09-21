/*
 * File:   Main.c
 * Author: staro
 *
 * Created on 12. April 2021, 16:00
 */


#include <xc.h>
#include <pic16f886.h>
#include "conbits.h"
#include <stdint.h>
#include <stdio.h>
#include "UART.h"
#include <string.h>

uint8_t mensaje[]="Hello\n";

void main(void) {
    UART_TX_Init(9600);
    while(1)
    {
        for(uint8_t a=0;a<strlen((char *)mensaje);a++)
        {
            UART_Write(mensaje[a]);
        }     
        __delay_ms(1000);
    }
    
    
    return;
}
