#include<iostream>

using namespace std;

void printArr(int myArr[], int arrSize){
    printf_s("待输出数组为：");
    for(int i = 0; i < arrSize; ++i)
        printf_s("%d ", myArr[i]);
    printf_s("\n");      
}

void printArr(double myArr[], int arrSize){
    printf_s("待输出数组为：");
    for(int i = 0; i < arrSize; ++i)
        printf_s("%f ", myArr[i]);
    printf_s("\n");      
}

template<class T>
void deleteArr(T * arr, const int size){
    for(int i = 0; i < size - 1; i++)
        *(arr + i) = '\0';
    
    arr = NULL;
    delete arr;
}

template<class T>
void freeArr(T * arr, const int size){
    for(int i = 0; i < size - 1; i++)
        *(arr + i) = '\0';
    
    free(arr);
}


int main(void){
    //定义数组的第1种方式：
    int myArr1[5];

    for(int i = 0; i < 5; ++i)
        myArr1[i] = (i + 1) * 10;
        
    printArr(myArr1, sizeof(myArr1) / sizeof(int));

    myArr1[3] *= 10;
    //printf_s("%d\n", myArr[-2]);
    printArr(myArr1, sizeof(myArr1) / sizeof(int));
    //此种定义方式不用删除数组

    //定义数组的第2种方式：
    int * myArr2 = myArr1;
    printArr(myArr2, 5);
    deleteArr(myArr2, 5);

    //定义数组的第3种方式：
    int * myArr3 = new int(5);

    //或者以下2种写法也是可以的：
    //int * myArr6{new int(5)};
    //int * myArr6{new int{5}};
    
    for(int i = 1; i <= 5; i++)
        *(myArr3 + i - 1) = i * 500;
    printArr(myArr3, 5);
    deleteArr(myArr3, 5);


    //定义数组的第4种方式：
    int * myArr4 = (int *)malloc(5 * sizeof(int));
    
    if(myArr4 == NULL){
        cout << "Memory not allocated!" << endl;
        free(myArr4);
    }

    for(int i = 1; i <= 5; i++)
        *(myArr4 + i - 1) = i * 100;
    printArr(myArr4, 5);
    freeArr(myArr4, 5);

    //定义数组的第5种方式：
    double * myArr5 = (double *)calloc(5, sizeof(double));
    
    if(myArr5 == NULL){
        cout << "Memory not allocated!" << endl;
        free(myArr5);
    }

    for(int i = 1; i <= 5; i++)
        *(myArr5 + i - 1) = i * 1.5;
    printArr(myArr5, 5);
    //freeArr(myArr5, 5);
    
    //定义数组的第6种方式：
    int * myArr6 = (int *)realloc(myArr5, 5 * sizeof(int));
    
    if(myArr6 == NULL){
        cout << "Memory not be reallocated!" << endl;
        free(myArr6);
    }

    for(int i = 1; i <= 5; i++)
        *(myArr6 + i - 1) = i * 1000;
    printArr(myArr6, 5);
    freeArr(myArr6, 5);
    
    system("pause");
    return 0;
}