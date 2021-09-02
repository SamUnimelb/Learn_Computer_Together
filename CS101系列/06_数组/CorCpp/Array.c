#include<stdio.h>

void printArr(int myArr[], int arrSize){
    printf_s("数组中的元素为：");
    for(int i = 0; i < arrSize; ++i)
        printf_s("%d ", myArr[i]);
    printf_s("\n");      
}

int main(void){
    int myArr[5];

    for(int i = 0; i < 5; ++i)
        myArr[i] = (i + 1) * 10;
        
    printArr(myArr, sizeof(myArr) / sizeof(int));

    myArr[3] *= 10;
    //printf_s("%d\n", myArr[-2]);
    printArr(myArr, sizeof(myArr) / sizeof(int));
    
    system("pause");
    return 0;
}