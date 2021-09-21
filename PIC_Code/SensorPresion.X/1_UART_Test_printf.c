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
#include <string.h>
#include "UART2.h"

void main(void) {
    UART_TX_Init(9600);
    uint16_t number= 1000;
    uint8_t buffer[10]; //To know the real size of only the string, we could use strleng()
    sprintf((char *)buffer,"%d\n",number);
    while(1)    
    {
        UART_Buffer(buffer,strlen((char *)buffer));
    }
    
    
    return;
}
