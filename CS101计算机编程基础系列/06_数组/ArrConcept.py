# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 21:09:59 2023
@author: Sam_Yan
"""

arr = [1, 4, 2, 3, 5]
arr2 = list(range(1, 6))

print(arr)
print(arr2)


for i in range(0, len(arr2)):
    arr2[i] *= 1.5
    
print(arr2)
