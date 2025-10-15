#include <stdio.h>
#include <stdint.h>

// Simple 16-bit one's complement checksum over input bytes (ASCII).
int main(){
    char buf[1024];
    printf("Enter message to compute checksum:\n");
    if(!fgets(buf,sizeof(buf),stdin)) return 0;
    // remove newline
    size_t n = strlen(buf);
    if(n && buf[n-1]=='\n') buf[n-1]=0, n--;
    uint32_t sum=0;
    for(size_t i=0;i<n;i+=2){
        uint16_t word = (uint8_t)buf[i];
        if(i+1<n) word = (word<<8) | (uint8_t)buf[i+1];
        sum += word;
        if(sum & 0x10000) sum = (sum & 0xFFFF) + 1;
    }
    uint16_t checksum = ~((uint16_t)sum);
    printf("Checksum (hex): 0x%04X\n", checksum);
    return 0;
}
