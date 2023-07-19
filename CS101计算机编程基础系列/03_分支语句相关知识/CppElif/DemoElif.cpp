#include<iostream>
#include<string>

using namespace std;

int main(){
    cout << "请输入你大一学的编程语言：";
    string progLan;
    cin >> progLan;

    if(progLan.compare("C") == 0 || progLan.compare("C++") == 0)
        cout << "系统架构专家" << endl;
    else if(progLan.compare("Java") == 0 )
        cout << "服务架构专家，或者多终端程序员" << endl;
    else if(progLan.compare("Python") == 0)
        cout << "AI和数据分析大师" << endl;
    else
        cout << "试试前端？" << endl;

    system("pause");
    return 0;
}