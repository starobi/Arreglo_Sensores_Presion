/*
 * File:   2_ADC_Test.c
 * Author: staro
 *
 * Created on 5. Mai 2021, 18:30
 */


#include <xc.h>
#include <pic16f886.h>
#include "conbits.h"


uint8_t mensaje[]="Programa Iniciado \n";
uint16_t AN_Read=0;

/*
void __interrupt() ISR(void)
{
   UART_number((int) ADC_ISR_handling());
}
 * 
 * */
void main(void) {
    UART_TX_Init(9600);
    UART_Buffer(mensaje, strlen(mensaje));
    while(1)
    {
        ADC_init_channel(4);
        while(ADCON0bits.GO_DONE);  // Polling GO_DONE = Delay Until Conversion Is Complete
        AN_Read = (ADRESH << 8) + ADRESL;
        UART_number((int)AN_Read);
    }
    
    
    return;
}
