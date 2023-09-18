#include<iostream>

using namespace std;

void printArr(const int * numArr, const int size){
    cout << "[";
    
    for(int i = 0; i < size - 1; i++)
        cout << numArr[i] << ", ";
    
    cout << numArr[size - 1] << "]" << endl;
    return;
}

int main(){
    int numArr1[] = {1, 3, 4, 5, 2};

    int numArr2[10];
    for(int i = 0; i < 10; i++)
        numArr2[i] = (i + 1) * 2;

    printArr(numArr1, 5);
    printArr(numArr2, 10);

    system("pause");
    return 0;
}




