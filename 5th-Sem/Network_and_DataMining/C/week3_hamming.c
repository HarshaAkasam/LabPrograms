#include <stdio.h>
#include <string.h>
#include <math.h>

// Generate Hamming(7,4) code for a 4-bit nibble input (as 0-15).
int main(){
    int data;
    printf("Enter 4-bit data as integer (0-15):\n");
    if(scanf("%d",&data)!=1) return 0;
    if(data<0||data>15){ printf("Invalid\n"); return 0;}
    int d[4];
    for(int i=0;i<4;i++) d[i] = (data >> i) & 1;
    // positions: 1-indexed: p1 p2 d1 p3 d2 d3 d4  -> bits 1..7
    int h[8];
    h[3]=d[0]; h[5]=d[1]; h[6]=d[2]; h[7]=d[3];
    h[1] = h[3] ^ h[5] ^ h[7];
    h[2] = h[3] ^ h[6] ^ h[7];
    h[4] = h[5] ^ h[6] ^ h[7];
    printf("Hamming(7,4) code bits (position 1..7): ");
    for(int i=1;i<=7;i++) printf("%d",h[i]);
    printf("\n");
    return 0;
}
