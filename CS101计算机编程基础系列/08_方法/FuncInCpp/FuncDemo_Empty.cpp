#include<stdio.h>
#include<iostream>
#include "FuncDemo.h"

using namespace std;

/*
* Pure C does not support function overloading,
* nor does it support passing by ref. 
* 
* Unfinished program, 
* For your own practice during the study,
* can learn these by following the video while typing. 
*/

int passByVal(int val){ //Pass by value

}

int passByVal(int val1, int val2){

}

double passByVal(double val1, double val2){

}

void passByPtr(int* p){//Pass by ptr / address

}

void passByRef(int &num){//Pss by ref, usually not recommended in C++

}

int main(void){
    int num = 123;
    passByVal(num);
    printf("num after pass by val is %d\n", num);
    passByPtr(&num);
    printf("num after pass by address/ptr is %d\n", num);
    passByRef(num);
    printf("num after pass by reference is %d\n", num);

    cout << "Number added by 100 is: " << passByVal(num, 100) << endl;
    cout << "Number times 2.5 is: " << passByVal(num * 1.0, 2.5) << endl;
    system("pause");
    return 0;
}