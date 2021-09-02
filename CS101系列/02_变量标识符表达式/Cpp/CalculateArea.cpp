#include<iostream>
#include<cmath>

using namespace std;

int main(){
    cout << "请输入半径: ";
    double radius = 0.0;
    cin >> radius;

    double area = M_PI * pow(radius, 2);
    cout << "圆的面积为：" << area << endl;

    system("pause");
    return 0;
}
