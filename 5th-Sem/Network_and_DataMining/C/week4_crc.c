#include <stdio.h>
#include <string.h>
#include <stdint.h>

// Simple bitwise CRC function for arbitrary polynomials represented as integer poly
uint32_t compute_crc(const uint8_t *data, size_t len_bits, uint32_t poly, int poly_degree){
    uint32_t reg = 0;
    for(size_t i=0;i<len_bits;i++){
        int bit = (data[i/8] >> (7 - (i%8))) & 1;
        reg = (reg << 1) | bit;
        if(reg & (1u << poly_degree)){
            reg ^= poly;
        }
    }
    return reg;
}

int main(){
    printf("This program demonstrates CRC-12, CRC-16 and CRC-CCITT computation for ASCII input.\n");
    char input[1024];
    printf("Enter text:\n");
    if(!fgets(input,sizeof(input),stdin)) return 0;
    size_t n = strlen(input);
    if(n && input[n-1]=='\n') input[n-1]=0, n--;
    // prepare bit array
    uint8_t buf[1024]={0};
    memcpy(buf,input,n);
    size_t bits = n * 8;
    // CRC-12 polynomial (x^12 + x^11 + x^3 + x^2 + x + 1) -> 0x80F? use common CRC-12 (0x80F)
    uint32_t crc12 = compute_crc(buf, bits, 0x80F, 12);
    // CRC-16-IBM polynomial 0x8005 degree 16 (we use 0x1021 for CCITT variant below)
    uint32_t crc16 = compute_crc(buf, bits, 0x8005, 16);
    // CRC-CCITT (x^16 + x^12 + x^5 + 1) poly 0x1021
    uint32_t crcccitt = compute_crc(buf, bits, 0x1021, 16);
    printf("CRC-12: 0x%X\nCRC-16: 0x%X\nCRC-CCITT: 0x%X\n", crc12, crc16, crcccitt);
    return 0;
}
