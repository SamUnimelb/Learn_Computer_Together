# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 22:10:14 2023

@author: Sam_Yan
"""

isSatisfiedInput = False

while not isSatisfiedInput:
    try:
        age = int(input("请亲告诉我一下年龄："))
        isSatisfiedInput = True
    except ValueError:
        print("请亲确定输入是个代表年龄的整数哟！")
    
print("输入的年龄为：{:3d}".format(age))