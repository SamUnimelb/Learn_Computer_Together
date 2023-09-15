#include<iostream>

using namespace std;

template<class T>
void printArr(T * arr, int size){
    for(int i = 0; i < size; i++)   
        cout << arr[i] << " ";
    cout << endl;
}

template<class T>
void deleteArr(T * arr, int size){
    for(int i = 0; i < size; i++)   
        arr[i] = '\0';
    
    arr = NULL;
    delete arr;
}

int main(){
    int numArr1[] = {1, 4, 2, 3, 5}; //数组的第一种定义方式。

    //数组的第二种定义方式
    double numArr2[5];
    for(int i = 0; i < 5; i++)
        numArr2[i] = i + 1;

    printArr(numArr1, 5);
    printArr(numArr2, 5);

    for(int i = 0; i < 5; i++)
        cout << numArr2[i] << ", Adress: " << &numArr2[i] << endl;

    for(int i = 0; i < 5; i++)
        numArr2[i] *= 1.5;
    printArr(numArr2, 5);
    
    int * ptr = numArr1;
    for(int i = 0; i < 5; i++)
        *(ptr + i) += 2;

    printArr(numArr1, 5);
    deleteArr(numArr1, 5);
    deleteArr(numArr2, 5);

    ptr = NULL;
    delete ptr;

    system("pause");
    return 0;
}