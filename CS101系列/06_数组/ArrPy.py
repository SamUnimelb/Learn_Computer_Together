# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 16:06:09 2021
@author: Sam_Yan
"""

class MyObject: pass

myArr = [1, 2, 3, "string", 'A', MyObject()]
#myArr = [(i + 1) * 10 for i in range(5)]
myArr.append(4)
myArr.remove('A')
print(myArr)
#myArr[3] *= 10
#print(myArr)

