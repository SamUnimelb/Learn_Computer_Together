#include<iostream>
#include<cctype>
#include <time.h>

using namespace std;

int main(){
    srand(time(NULL));
    cout << (rand() % 100) / 100.0 << endl;
    /*int grade{0};
    cout << "Input your grade: ";
    cin >> grade;
    //string output = (grade >= 60? "passed":"failed");
    int output = (grade >= 60? 1:0);
    cout << output << endl;*/

    /*cout << "Input your ladder grade: ";
    string ladderGrade;
    cin >> ladderGrade;

    switch (toupper(ladderGrade[0]))
    {
    case 'A':
        cout << "很优秀，一直保持这个成绩考研很有希望呀！" << endl;
        switch(toupper(ladderGrade[1])){
            case '+':
                cout << "GPA = 4.3，未来妥妥的这方面专家哦！" << endl; break;
            case '-':
                cout << "GPA = 3.7，高级业余组成员哦！" << endl; break;
            default:
                cout << "GPA = 4.0，未来妥妥的这方面专家哦！" << endl; break;
        }
    case 'B':
        if(toupper(ladderGrade[0]) != 'A'){
            cout << "本门课业余组成员，想在这方面考研的话仍需努力哦！" << endl;
            switch(toupper(ladderGrade[1])){
                case '+':
                    cout << "GPA = 3.3，高级业余组成员哦！" << endl; break;
                case '-':
                    cout << "GPA = 2.7，这个水平已经很业余了！" << endl; break;
                default:
                    cout << "GPA = 3.0，一般业余组成员哦！" << endl; break;
            }
        }
    case 'C':
        if(toupper(ladderGrade[0]) != 'A' && toupper(ladderGrade[0]) != 'B'){
            cout << "你在这课的水平很业余了，建议考研别往这方面想哦！" << endl;
            switch(toupper(ladderGrade[1])){
                case '+':
                    cout << "GPA = 2.3，正常听课交作业考试的一个成绩。" << endl; break;
                default:
                    cout << "GPA = 2.0，正常听课交作业考试还错得比较多的一个成绩。" << endl; break;
            }
        }
    case 'P':
        //C-是挂了的。
        if(toupper(ladderGrade[1]) != 'C' && toupper(ladderGrade[1]) != '-')
            cout << "恭喜你这门课过了！" << endl;     
        break;
    default:
        cout << "很不幸这门课你挂了！" << endl;
        break;
    }*/

    system("pause");
    return 0;
}
