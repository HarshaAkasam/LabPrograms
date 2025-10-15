#include <stdio.h>
#include <string.h>

// Simple bit stuffing for an input bit string (e.g., 011111101)
// Insert a '0' after five consecutive '1's during transmission.

int main(){
    char input[2048];
    printf("Enter bit string (0/1 only):\n");
    if(!fgets(input,sizeof(input),stdin)) return 0;
    size_t n=strlen(input);
    if(n && input[n-1]=='\n') input[n-1]=0;
    int count=0;
    printf("Transmitted (with stuffing): ");
    for(size_t i=0;i<strlen(input);++i){
        char c = input[i];
        putchar(c);
        if(c=='1') count++; else count=0;
        if(count==5){
            putchar('0'); // stuffed bit
            count=0;
        }
    }
    printf("\n");
    // Destuff
    printf("Receiver (after destuffing): ");
    count=0;
    for(size_t i=0;i<strlen(input);++i){
        char c = input[i];
        if(c=='1') count++; else count=0;
        putchar(c);
        if(count==5){
            // next bit in transmitted was stuffed '0' - skip it in destuffing
            i++; // skip stuffed bit
            count=0;
        }
    }
    printf("\n");
    return 0;
}
