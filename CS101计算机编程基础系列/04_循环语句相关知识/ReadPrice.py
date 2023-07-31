# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 09:48:05 2023

@author: Sam_Yan
"""

import re

isSatisfiedInput = False

while not isSatisfiedInput:
    try:
        priceStr = input("请亲输入物品价格: ")
        
        # Test of regular expressions available at: https://regex101.com/
        ret = re.match(re.compile("^\d*(.\d{1,2})?$"), priceStr)
        
        if not ret:
            raise ValueError("请亲确定物品价格输入正确哟！")
            
        price, isSatisfiedInput = float(priceStr), True
            
    except ValueError as e:
        print(e)

print(price)