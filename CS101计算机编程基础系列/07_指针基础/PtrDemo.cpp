#include<iostream>

using namespace std;

int main(){
    /*int num = 123;
    int* p = &num;
    
    cout << "num is: " << num << ", *p is: " << *p << endl;
    cout << "Value of p is: " << p << ", &num is: " << &num << endl;

    *p = 100;
    cout << "num is: " << num << ", *p is: " << *p << endl;
    cout << "Value of p is: " << p << ", &num is: " << &num << endl;*/

    int myArr[5];
    for(int i = 0; i < 5; ++i)
        myArr[i] = (i + 1) * 10;
    int* p = myArr;

    cout << "p is: " << p << ", myArr is: " << myArr <<
        ", and &myArr[0]" << &myArr[0] << endl;

    for(int i = 0; i < 5; ++i)
        cout << p[i] << " ";
    cout << endl;

    /*p = nullptr;
    cout << "p is: " << p << endl;*/

    string ptr[] = {"first", "second", "third"};
    for(int i = 0; i < 3; ++i)
        cout << ptr[i] << " ";
    cout << endl;

    system("pause");
    return 0;
}