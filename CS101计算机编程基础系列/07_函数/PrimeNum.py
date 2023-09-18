# -*- coding: utf-8 -*-
"""
Created on Sat Jul 29 19:32:39 2023
@author: Sam_Yan
"""

# print(isinstance(5, int))


def isPrime(num:int):
    if (not isinstance(num, int)) or num <= 1:
        raise TypeError("待判别参数必须是一个大于1的整数")
    
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    
    return True


def getIntInput():
    isSatisfiedInput = False
    
    while not isSatisfiedInput:
        try:
            num = int(input("请亲输入一个需要判别是否素数的整数："))
        
            if num <= 1:
                raise ValueError("请亲输入一个大于1的整数哟！")
        
            isSatisfiedInput = True
            
        except ValueError:
            print("请亲确定输入的是一个需要判别是否素数的整数哦！")
    
    return num
            
if __name__ == "__main__":
    ret = "这个整数是个素数" if isPrime(getIntInput()) else "这个整数它是个合数"
    print(ret)
    




