# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 09:48:05 2023
@author: Sam_Yan
"""

import re

isSatisfiedInput = False

while not isSatisfiedInput:
    priceStr = input("请亲输入物品价格: ")
        
    # Test of regular expressions available at: https://regex101.com/
    ret = re.match(re.compile("^\d*(.\d{1,2})?$"), priceStr)
        
    if ret: price, isSatisfiedInput = float(priceStr), True
    else: print("请亲确定物品价格输入正确哟！")

print(f"正确输入的价格为：{price:.2f}")