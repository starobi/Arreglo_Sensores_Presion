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


uint8_t mensaje[]="Programa Iniciado\n";
uint8_t ANChannels[]={12,10,8,9,11,13,1,0}; 
uint16_t ANRead[8];
void main(void) {
    UART_TX_Init(230400); //Maximum Speed 230400
    UART_Buffer(mensaje, strlen(mensaje));
    //TRISC1=0; //PORTC 1 output to Measure Transmision Time with Logic Analyzer 
    //TRISC2=0; //PORTC 2 output to Measure Sampling Time
    while(1)
    {
        //RC1=1; 
        //RC2=1,
        ADC_burst(ANChannels,ANRead,8);
        //RC2=0;
        ADC_print_burst(ANRead,8);
        //RC1=0;
        __delay_ms(17.38); //Delay to have a total Transmission of 20ms
    }
    return;
}
