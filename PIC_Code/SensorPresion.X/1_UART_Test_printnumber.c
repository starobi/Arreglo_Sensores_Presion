#include <xc.h>
#include <pic16f886.h>
#include "conbits.h"
#include <stdint.h>
#include <stdio.h>
#include <string.h>
#include "UART2.h"

void main(void) {
    UART_TX_Init(9600);
    int a = 23567;
    while(1)    
    {
        
        UART_number(a);
    }
    
    
    return;
}
