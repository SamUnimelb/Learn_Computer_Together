#include<iostream>

using namespace std;

int main(){
    cout << "请输入分数：";
    int mark;
    cin >> mark;

    if(mark >= 594){
        cout << "考上很好的学校" << endl;
        cout << "稍微学习一下" << endl;
    }else{
        printf("%s\n", "考上一般的学校");
        printf("%s\n", "通过及其努力的学习、积极参与实习和项目");
        printf("%s\n", "准备简历、锤炼技术、努力应聘");
    }


    cout << "成为大厂技术大牛" << endl;
    cout << "迎娶白富美" << endl;
    cout << "走上人生巅峰" << endl;

    system("pause");
    return 0;
}