#include<math.h>
#include<sys/time.h>
#include<stdio.h>

int main(void){
    struct timeval stop, start;
    gettimeofday(&start, NULL);
    double x = 0.0, fx;
    
    while(x <= 10000.0){
        fx = x * sin(x);
        x += pow(2, -8);
        //printf("%f\n", fx);
    }

    gettimeofday(&stop, NULL);
    double timeInMs = ((stop.tv_sec - start.tv_sec) * 1000000 + stop.tv_usec - start.tv_usec) / 1000.0;
    printf("took %.2f ms\n",  timeInMs);
}