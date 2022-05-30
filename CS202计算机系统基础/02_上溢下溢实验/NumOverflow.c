#include <stdio.h>
#include <math.h>

void main(){
    unsigned int bigInt1 = pow(2, 32) - 1;
    printf("The unsigned big integer is: %u\n", bigInt1);
    bigInt1 ++;
    printf("The unsigned big integer is: %u\n", bigInt1);

    int bigInt2 = pow(2, 31) - 1;
    printf("The big integer is: %d\n", bigInt2);
    bigInt2++;
    printf("The big integer is: %d\n", bigInt2);

    int bigInt3 = -pow(2, 31);
    printf("The big integer is: %d\n", bigInt3);
    bigInt3--;
    printf("The big integer is: %d\n", bigInt3);
}