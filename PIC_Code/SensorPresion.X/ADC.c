/*
 * File:   ADC.c
 * Author: staro
 *
 * Created on 5. Mai 2021, 18:40
 */


#include "ADC.h"
#include <stdint.h>
#include <xc.h>
#include <pic16f886.h>
#include "conbits.h"

uint16_t AN0_RES;


//Iniciar convesión de un canal analógico
void ADC_init_channel(char channel)
{
    //Turn on and Select channel
    ADCON0 = 0x81;  // Turn ADC ON, and diveide FOSC/32 to obtain a Tad= 2us
    ADCON1 = 0x80; //  Result is "Right-Justified" 
    ADCON0 |= (channel<<2); //Channel selection
    
    //Wait for the Time acquisition
    __delay_us(5);  // The Minimum Tacq = 5us
    
    //Star ADC conversion
    GO_DONE = 1;  // Start A/D Conversion
}

//Iniciar conversión canal analógico con interrupción
//Arguments:

void ADC_init_channel_IR(char channel)
{
    //Turn on and Select channel
    ADCON0 = 0x81;  // Turn ADC ON, and diveide FOSC/32 to obtain a Tad= 2us
    ADCON1 = 0x80; //  Result is "Right-Justified" 
    ADCON0 |= (channel<<2); //Channel selection
    //RA5 Channel 4
   
    //Configure Interrupts
    ADIF = 0;  // Clear ADC Interrupt Flag
    ADIE = 1;  // ADC Interrupt Enable Bit
    PEIE = 1;  // Peripherals Interrupt Enable Bit
    GIE = 1;   // Global Interrupts Enable Bit
    
    
    //Wait for the Time acquisition
    __delay_us(30);  // The Minimum Tacq = 20us, So That should be enough
    
    //Star ADC conversion
    GO_DONE = 1;  // Start A/D Conversion
}

// Conversión de varios canales analógicos indicados en un pointer o arreglo. Las mediciones se guardan en un arreglo. 
void ADC_burst(uint8_t *channels,uint16_t *reading,uint8_t numberc)
{
    for(uint8_t n=0;n<numberc;n++ )
    {
        ADC_init_channel(channels[n]);
        while(ADCON0bits.GO_DONE); 
        reading[n] = (ADRESH << 8) + ADRESL;
    }
}

//Print the burst readings into ASCI. 
void ADC_print_burst(uint16_t *BurstReadings, uint8_t NumberReadings)
{
    for(uint8_t n=0; n<NumberReadings;n++)
        {
            UART_number((int)BurstReadings[n]);
        }
    UART_Write(SPACE);
    
}


//Function to handle the interruption due to end of transmission
uint16_t ADC_ISR_handling(void)
{
    uint16_t AN_Read;
      if(ADIF)
  {
    // Read A/D Conversion Result Registers ADRESH, ADRESL
    // Clear The ADC Interrupt Flag Bit
    ADIF = 0;
    AN_Read = (ADRESH << 8) + ADRESL; // Read The Right-Justified 10-Bit Result
    return AN_Read;
  }
}





