#include<iostream>
#include<string>

using namespace std;

/*
template<class T>
void printLst(T lst[], int size){
    for(int i = 0; i < size; i++)
        cout << lst[i] << endl;

//Does not work:
    for(T each : lst)
        cout << each << endl;
}*/

template<class T>
void printLst(const T * lst, const int size){
    cout << "{";
    for(int i = 0; i < size - 1; i++)
        cout << *(lst + i) << ", ";
    cout << *(lst + size - 1);
    cout << "}" << endl;
}

template<class T>
void deleteLst(T * lst, const int size){
    for(int i = 0; i < size - 1; i++)
        *(lst + i) = '\0';
    
    lst = NULL;
    delete lst;
}

int main(){
    string actions[] = {u8"关注", u8"点赞", u8"转发", u8"收藏", u8"订阅"};
    
    for(string action : actions)
        cout << action << endl;
    cout << endl;

    printLst(actions, 5);

    for(string action : actions)
        action = u8"白嫖";
    
    printf("\n");
    printLst(actions, 5);

    for(int i = 0; i < 5; i++)
        actions[i] = u8"白嫖成功！";
    printf("\n");
    printLst(actions, 5);

    deleteLst(actions, 5);

    //Testing code:
    double myArr[5] = {1.25, 1.5, 1.75, 2, 2.5};
    printLst(myArr, 5);
    deleteLst(myArr, 5);

    system("pause");
    return 0;

}
