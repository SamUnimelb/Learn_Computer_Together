# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 22:44:44 2021
@author: Sam_Yan
"""

def passByVal(val1, val2=None):
    if val2 == None:
        val1 = 888
        return

    if type(val1) == float and type(val2) == float:
        return val1 * val2
    
    return val1 + val2

class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y
    def __str__(self):
        return "Point is: (" + str(self.x) + ", " + str(self.y) + "). "
    
def passByRef(p):
    p.x, p.y = 1.0, 1.0
    

if __name__ == "__main__":
    num = 123
    passByVal(num)
    print("After func call num is " + str(num))
    num = passByVal(num, 100)
    print("After func call num is " + str(num))
    num = passByVal(num * 1.0, 2.5)
    print("After func call num is " + str(num))
    
    p = Point(0, 0)
    passByRef(p)
    print(p)
    