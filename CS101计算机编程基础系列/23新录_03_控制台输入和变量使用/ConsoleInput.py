# -*- coding: utf-8 -*-
"""
Created on Sat Jul 15 18:26:58 2023
@author: Sam_Yan

从控制台获取两个整数、一个浮点数（作为圆的半径）
然后把两个整数之和
和圆的面积输出到控制台
"""

import math

num1 = int(input("请输入第一个整数："))
# print(type(num1))
num2 = int(input("请输入第二个整数："))
print("num1 + num2 = " + str(num1 + num2))

radius = float(input("请输入圆的半径："))
area = math.pi * radius ** 2
print("圆的面积为： " + str(area))
