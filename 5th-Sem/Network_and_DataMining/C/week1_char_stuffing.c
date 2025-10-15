#include <stdio.h>
#include <string.h>

// Simple character stuffing using flag "$" and escape "\".
// Input: frame string from stdin. Output: stuffed frame printed.

int main() {
    char input[1024];
    printf("Enter data to send (no newline):\n");
    if(!fgets(input, sizeof(input), stdin)) return 0;
    // remove newline
    size_t n = strlen(input);
    if(n && input[n-1]=='\n') input[n-1]=0;
    printf("Sender side:\n");
    printf("FLAG$");
    for(size_t i=0;i<strlen(input);++i){
        if(input[i]=='$' || input[i]=='\\'){
            putchar('\\'); // escape
        }
        putchar(input[i]);
    }
    printf("$FLAG\n");
    printf("Receiver side (destuffing):\n");
    // destuff
    char *p = input;
    int i=0;
    while(p[i]){
        if(p[i]=='\\' && p[i+1]){
            putchar(p[i+1]);
            i+=2;
        } else {
            putchar(p[i]);
            i++;
        }
    }
    printf("\n");
    return 0;
}
