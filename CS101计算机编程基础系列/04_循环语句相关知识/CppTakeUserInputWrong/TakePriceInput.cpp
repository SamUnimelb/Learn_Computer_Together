#include <iostream>
#include <sstream>
#include <string>
#include <math.h>

using namespace std;

bool isFloat(string myString){
    std::istringstream iss(myString);
    float f;
    iss >> noskipws >> f; // noskipws considers leading whitespace invalid
    // Check the entire string was consumed and if either failbit or badbit is set
    //cout << "In function: " << (iss.eof() && !iss.fail()) << endl;
    //system("pause");
    return iss.eof() && !iss.fail(); 
}

int main(){
 
    string priceStr;
    double price = 0.0;
    bool isSatisfiedInput = false;

    do{
        cout << "请输入物品的价格（元）: ";
        cin >> priceStr;
        try{
            //cout << "In main: " << isFloat(priceStr) << endl;
            
            if(isFloat(priceStr)){
                price = stof(priceStr);
                double checkedPrice = int(price * 100) / 100.0;

                if(price != checkedPrice)
                    throw(price);
                
                isSatisfiedInput = true;

            }else{
                //cout << "In else: " << endl;
                //system("pause");
                
                /*
                //C++中的catch子句区分处理对象是string和const char *
                //所以实现中要么catch子句处理类型为const char *，
                //要么抛出时将类型转化为string。
                throw(string("请亲确定输入的是个数哦！"))*/;

                throw("请亲确定输入的是个浮点数哦！");
            }
        }/*catch(string typeErr){
            cout << typeErr << endl;
            system("pause");*/
        catch(const char * typeErr){
            cout << typeErr << endl;
        }catch(double wrongPrice){
            cout << "物品价格格式错误哦！" << endl;
        }
    }while(!isSatisfiedInput);

    printf("正确输入的价格为：%.2f\n", price);

    system("pause");
    return 0;
}