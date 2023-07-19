# -*- coding: utf-8 -*-
"""
Created on Sun Jul 16 20:50:34 2023

@author: Sam_Yan
"""

progLan = input("请输入你大一学的编程语言：")

match progLan:
    case "C" | "C++":
        print("系统架构专家")
    case "Java":
        print("服务架构专家，或者多终端程序员")
    case "Python":
        print("AI和数据分析大师")
    case _:
        print("试试前端？")
            
    