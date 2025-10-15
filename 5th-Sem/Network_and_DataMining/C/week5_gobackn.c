#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// Simulated Go-Back-N sender only.
// Send N frames, window size = W. Randomly simulate ACK loss.

int main(){
    int total_frames = 20;
    int W = 4;
    int base = 0, nextseq = 0;
    srand((unsigned)time(NULL));
    while(base < total_frames){
        // send frames in window
        while(nextseq < base + W && nextseq < total_frames){
            printf("Sending frame %d\n", nextseq);
            nextseq++;
        }
        // simulate waiting for ACK with random loss
        int r = rand() % 100;
        if(r < 70){
            // ACK for all up to nextseq-1
            int ack = nextseq - 1;
            printf("Received ACK %d\n", ack);
            base = ack + 1;
        } else {
            // timeout, go back
            printf("Timeout. Go-Back-N: retransmitting from %d\n", base);
            nextseq = base;
        }
    }
    printf("All frames sent and acknowledged.\n");
    return 0;
}
