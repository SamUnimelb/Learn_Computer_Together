# -*- coding: utf-8 -*-
"""
Created on Sat Jul 29 19:32:39 2023
@author: Sam_Yan
"""

isSatisfiedInput = False

while not isSatisfiedInput:
    try:
        num = int(input("请亲输入一个需要判别是否素数的整数："))
        
        if num <= 1:
            raise ValueError("请亲输入一个大于1的整数哟！")
        
        isSatisfiedInput = True
    except ValueError:
        print("请亲确定输入的是一个需要判别是否素数的整数哦！")

for i in range(2, int(num ** 0.5) + 1):
    if num % i == 0:
        print("这个整数它是个合数")
        break
else:
    print("这个整数是个素数")


