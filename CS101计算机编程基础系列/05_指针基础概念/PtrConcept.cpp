#include<iostream>

using namespace std;

int main(){

    int num = 666;
    cout << "num is: " << num << endl;

    cout << "The address of num is: " << &num << endl;

    int *ptr = &num;
    cout << ptr << endl;

    *ptr = 888;
    cout << "New num is: " << num << endl;

    free(ptr);

    system("pause");
    return 0;
}