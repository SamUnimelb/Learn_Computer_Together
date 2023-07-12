#include<iostream>
#include<string>

using namespace std;

class Person{
private:
    string name;

public:
    Person(string name){
        this->name = name;
    }

    string getName(){
        return name;
    }

};

int main(){
    Person jason("Jason");
    cout << "Welcome, " << jason.getName() << "!" << endl;
    system("pause");
    return 0;
}

