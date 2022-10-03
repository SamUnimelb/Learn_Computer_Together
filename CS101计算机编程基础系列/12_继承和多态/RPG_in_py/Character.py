# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 16:09:14 2022
@author: Sam Yan
"""

class Character:    
    def __init__(self, name, gender, age, gang):
        self.__name, self.__gender, self.__age, self.__gang = (
            name, gender, age, gang)
    
    def getName(self):
        return self.__name
    
    def getGender(self):
        return self.__gender
    
    def getAge(self):
        return self.__age
    
    def getGang(self):
        return self.__gang
    
    def __str__(self):
        return "游戏人物名称：" + self.__name + "，所属剧情：" + self.__gang
        
 
class Onmyoji(Character):
     def __init__(self, name, gender, age):
        Character.__init__(self, name, gender, age, "阴阳师人物")
 
class XianjianCharacter(Character):
     def __init__(self, name, gender, age, gang="仙剑人物"):
        Character.__init__(self, name, gender, age, gang)


if __name__ == "__main__":
    xuejian = XianjianCharacter("唐雪见", 'F', 32, "仙剑奇侠传-唐门")
    #print(xuejian.getName() + "属于" + xuejian.getGang())
    print(xuejian)
    
    xiaoyao = XianjianCharacter("李逍遥", 'M', 34)
    print(xiaoyao.getName() + "属于" + xiaoyao.getGang())
   