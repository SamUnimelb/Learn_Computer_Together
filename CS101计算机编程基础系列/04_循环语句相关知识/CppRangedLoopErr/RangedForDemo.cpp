#include<iostream>

using namespace std;

//Wrong versions that does not work are commented.
//Reasons to be explored.
/*void printLst(string &arr){
    for(string each : arr)
        cout << each << endl;
}*/

/*void printLst(string arr[]){
    for(string each : arr)
        cout << each << endl;
}*/

/*void printLst(string * arr){
    for(string each : arr)
        cout << each << endl;
}*/

void printList(string * arr, const int size){
    string localArr[size];
    for(int i = 0; i < size; i++)
        localArr[i] = *(arr + i);

    for(string s : localArr)
        cout << s  << " ";
    cout << endl;
}

int main(){
    string actions[] = {u8"关注", u8"点赞", u8"转发", u8"收藏", u8"订阅"};
    
    for(string action : actions)
        cout << action << endl;
    cout << endl;

    //printLst(actions); //Does not work
    printList(actions, 5);

    system("pause");
    return 0;

}