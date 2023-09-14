#include<iostream>

using namespace std;

template<class T>
void printArr(T * arr, int size){
    for(int i = 0; i < size; i++)   
        cout << arr[i] << " ";
    cout << endl;
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

int main(){
    //定义数组的第1种方式：
    int myArr1[] = {1, 2, 3, 4, 5};
    printArr(myArr1, sizeof(myArr1) / sizeof(int));

    //定义数组的第2种方式
    int myArr2[5];
    for(int i = 0; i < 5; ++i)
        myArr2[i] = (i + 1) * 10;        
    printArr(myArr1, sizeof(myArr1) / sizeof(int));

    myArr1[3] *= 10;
    //printf_s("%d\n", myArr[-2]);
    printArr(myArr1, sizeof(myArr1) / sizeof(int));
    //以上此种定义方式不用删除数组

    //定义数组的第3种方式：
    int * myArr3 = myArr1;
    printArr(myArr3, 5);
    deleteArr(myArr3, 5);

    //第4种定义方式
    int * myArr4 = new int(5); // int * myArr4{new int(5)};
    for(int i = 1; i <=5; i++)
        *(myArr4 + i - 1) = i * 500;
    printArr(myArr4, 5);
    deleteArr(myArr4, 5);

    //第5种定义方式
    int * myArr5 = (int *)malloc(5 * sizeof(int));

    if(myArr5 == NULL){
        cout << "空间未分配！" << endl;
        free(myArr5);
    }

    for(int i = 1; i <=5; i++)
        *(myArr5 + i - 1) = i * 100;
    printArr(myArr5, 5);
    freeArr(myArr5, 5);

    //第6种定义方式：
    double * myArr6 =  (double *)calloc(5, sizeof(double));
    if(myArr6 == NULL){
        cout << "空间未分配！" << endl;
        free(myArr6);
    }
    for(int i = 1; i <=5; i++)
        *(myArr6 + i - 1) = i * 1.5;
    printArr(myArr6, 5);
    

    //第7种定义方式：
    int * myArr7 = (int *)realloc(myArr6, 5 * sizeof(int));
    //freeArr(myArr6, 5);

    for(int i = 1; i <=5; i++)
        *(myArr7 + i - 1) = i * 1000;
    printArr(myArr7, 5);
    freeArr(myArr7, 5);

    system("pause");
    return 0;
}