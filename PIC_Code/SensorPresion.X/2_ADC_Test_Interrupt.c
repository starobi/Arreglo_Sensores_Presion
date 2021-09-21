/*
 * File:   2_ADC_Test_Interrupt.c
 * Author: staro
 *
 * Created on 18. Mai 2021, 15:32
 */
#include <xc.h>
#include <pic16f886.h>
#include "conbits.h"

uint8_t mensaje[]="Programa Iniciado \n";


void __interrupt() ISR(void)
{
   UART_number((int) ADC_ISR_handling());
}
 

void main(void) {
    UART_TX_Init(9600);
    UART_Buffer(mensaje, strlen(mensaje));
    
    while(1)
    {
        ADC_init_channel_IR(4);
        __delay_ms(1000);
    }
    
    return;
}
