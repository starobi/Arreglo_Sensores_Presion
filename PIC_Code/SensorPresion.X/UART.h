// This is a guard condition so that contents of this file are not included
// more than once.  
#ifndef UART_H
#define	UART_H


#include <xc.h> // include processor files - each processor file is guarded.  
#include <stdint.h>
#include <pic16f886.h>

//Useful ASCI MACROS FOR UART   
#define SPACE   10


void UART_TX_Init(uint32_t baud);
void UART_Write(uint8_t data);
uint8_t UART_TX_Empty(void);
void UART_Buffer(uint8_t *buffer, uint8_t size);
void UART_number(int number);


#endif	/* XC_HEADER_TEMPLATE_H */
