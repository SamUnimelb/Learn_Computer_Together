# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 18:16:14 2021
@author: Sam_Yan
"""
import math

while True:
    n = int(input("请输入一个正整数，输入小于等于1的整数退出: "))
    if n <= 1: break
    
    """
    while divisor <= math.sqrt(n): 
        #a = sqrt(n)
        #if n // a = b, b <= sqrt(n)
        if n // divisor == n / divisor:
            print("This is not a prime number!")
            break
        divisor += 1
    """
    for divisor in range(2, int(math.sqrt(n)) + 1):
        if n // divisor == n / divisor:
            print("This is not a prime number!")
            break
    else:
        print("This is a prime number!")