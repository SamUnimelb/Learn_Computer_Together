#include<iostream>

using namespace std;

int main(){

    int iArr[] = {5, 4, 3, 2, 1};
    int *iPtr = iArr;

    for(int i = 0; i < 5; i++)
        printf("Add: %x, Val: %d\n", iPtr + i, *(iPtr + i));

    double dArr[] = {0.25, 0.5, 1, 1.25,  1.5};
    double *dPtr = dArr;

    for(int i = 0; i < 5; i++)
        printf("Add: %x, Val: %f\n", dPtr + i, *(dPtr + i));

    system("pause");
    return 0;
}