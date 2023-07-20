#include<iostream>

using namespace std;

int main(){
    cout << "请输入表示大一学的编程语言的相关整数，1 - C/C++，2 - Java, 3 - Python，4 - 其他：";
    int progLan;
    cin >> progLan;

    switch(progLan){
        case 1:
            printf("%s\n", "系统架构专家");
        break;

        case 2:
            printf("%s\n", "服务架构专家，或者多终端程序员");
        break;

        case 3:
            printf("%s\n", "AI和数据分析大师");
        break;

        default:
            printf("%s\n", "试试前端");

    }

    system("pause");
    return 0;
}