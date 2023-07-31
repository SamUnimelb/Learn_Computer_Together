#include <iostream>
#include <regex>
#include <string>

using namespace std;

int main(){

    string priceStr;
    double price = 0.0;
    bool isSatisfiedInput = false;

    do{
        cout << "请输入物品的价格（元）: ";
        cin >> priceStr;

        regex priceMatch(R"(^\d*(.\d{1,2})?$)");

        if(regex_match(priceStr, priceMatch)){
            price = stof(priceStr);
            isSatisfiedInput = true;
        }else{
            printf("%s\n", "请亲确定输入的是个正确的表示价格的数哦！");
        }

    }while(!isSatisfiedInput);

    printf("正确输入的价格为：%.2f\n", price);

    system("pause");
    return 0;
}