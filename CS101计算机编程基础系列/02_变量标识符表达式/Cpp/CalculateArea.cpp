#include<iostream>
#include<cmath>

using namespace std;

int main(){
    printf("%s", "请输入两个整数，用空格隔开：");
    int num1, num2;
    scanf("%d %d", &num1, &num2);

    /*cout << "请输入第二个整数：";
    int num2;
    cin >> num2;*/

    //cout << "两个整数的和是：" << num1 + num2 << endl;

    printf("两个整数的和是：%d\n", (num1 + num2));

    cout << "请输入圆的半径: ";
    double radius = 0.0;
    cin >> radius;

    double area = M_PI * pow(radius, 2);
    cout << "圆的面积是：" << area << endl;

    system("pause");
    return 0;
}
