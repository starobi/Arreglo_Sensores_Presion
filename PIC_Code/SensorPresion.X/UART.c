/*
 * File:   UART.C
 * Author: staro
 *
 * Created on 30. April 2021, 17:38
 */


#include "UART.h"
#include <string.h>
#include <stdio.h>

//Configuración UART
void UART_TX_Init(uint32_t baud)
{
  //Calculate value for Baud rate. It works until 57600 Baud/s
  uint8_t temp;
  temp= (uint8_t)(((16000000/baud)/16)-1); // Formula to calcula SPBRG with high speed baud rate
  BRGH = 1; // Set For High-Speed Ba    ud Rate
  SPBRG = temp; // Set The Baud Rate To Be 9600 bps
  //--[ Enable The Ascynchronous Serial Port ]--
  SYNC = 0;
  SPEN = 1;
  //--[ Set The RX-TX Pins to be in UART mode (not io) ]--
  TRISC6 = 1;  // UART TX pin as input as stated in Datasheet
  TXEN = 1; // Enable UART Transmission
}

//Send 8 bits
void UART_Write(uint8_t data)
{
  while(!TRMT); //High while TXREG full
  TXREG = data;
}

//Function to check if the TX buffer is already sent
uint8_t UART_TX_Empty(void)
{
  // Check the output (transmitter) buffer emptiness
  return TRMT;
}

//Send a array of characters describing also the number of bytes.
void UART_Buffer(uint8_t *buffer, uint8_t size)
{
    char count=0;
    while(count<size)
    {
        UART_Write(*buffer);
        count++;
        buffer++;
    }
}

//Make conversion from number to array of ASCI at the end with a new line and send it
void UART_number(int number)
{
 uint8_t buffer[10]; //To know the real size of only the string, we could use strleng()
 sprintf((char *)buffer,"%d\n",number);  
 UART_Buffer(buffer,strlen((char *)buffer));
}