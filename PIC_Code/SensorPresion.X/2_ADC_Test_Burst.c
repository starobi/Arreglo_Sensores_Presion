/*
 * File:   2_ADC_Test_Burst.c
 * Author: staro
 *
 * This Program Sends a ADC burst through UART
 * Created on 19. Mai 2021, 10:25
 */

// Canales para ADC AN2 y AN3 son para REF+ y REF-
// Canal AN4, AN12, AN10,AN8, AN9, AN 11, AN12,AN13
#include <xc.h>
#include <pic16f886.h>
#include "conbits.h"


uint8_t mensaje[]="Programa Iniciado \n";
uint8_t ANChannels[]={12,10,8,9,11,13,4,3}; //AN9 gave problems, when i connect it UART stops working. I dont know it has a connection wihth UART. Verificar si es porque tiene otra funcionalidad por default. 
uint16_t ANRead[8];
void main(void) {
    OSCCON=(0b111)<<(4);// Change Oscillator to 8Mhz
    UART_TX_Init(115200);
    UART_Buffer(mensaje, strlen(mensaje));
    TRISC1=0; //PORTC 1 output
    TRISC2=0; //PORTC 1 output
    while(1)
    {
        RC1=1; //PIN C1 High
        RC2=1,
        ADC_burst(ANChannels,ANRead,8);
        RC2=0;
        ADC_print_burst(ANRead,8);
        RC1=0; //PIN C1 LOW
        __delay_ms(100);
    }
    return;
}
