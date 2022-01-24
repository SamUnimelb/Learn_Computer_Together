# -*- coding: utf-8 -*-
"""
Created on Sun Dec 19 10:00:46 2021
@author: Sam Yan
然后以此为模板，写一个针对所有实体和关系的处理器。
"""

from DBLinker import *
import re

def checkTimeLogic(startTime, finishTime):
    """Check if start time is earlier than finish time,
    time input as strings in format: YYYY-MM-DD HH:MM:SS"""
    #print(startTime)
    digits = re.compile("(\d+)+")
    startTimeNums = digits.findall(startTime)
    startTimeNums = [int(ele) for ele in startTimeNums]
    finishTimeNums = digits.findall(finishTime)
    finishTimeNums = [int(ele) for ele in finishTimeNums]
    if startTimeNums == finishTimeNums: return False
    
    for i, j in zip(startTimeNums, finishTimeNums):
        if i > j: return False
    
    return True
    

def checkTable(tableName, pkDict={}, colNames=[], retHeader="", varNames=[]):
    """需要传入：tableName - 数据表名称，pkDict - 主键值对，
    colNames - 要选择以及呈现的几列，retHeader - 输出结果说明信息头（行）,
    varNames - 输出变量应呈现为什么中文 - {colName : "中文栏名"}    
    """
    condstr, colNamestr = "TRUE", "*"
    
    if pkDict != {}:
        condstr = ""
        for k in pkDict.keys():
            condstr += str(k) + " = '" + str(pkDict[k]) + "' AND "
        condstr += " TRUE "
        
    if colNames != []:
        colNamestr = ""
        for name in colNames[:-1]:
            colNamestr += str(name) + ", "
        colNamestr += colNames[-1]
        
    selector = Selector(tableName, colNamestr=colNamestr, condstr=condstr)
    ret = selector.returnRets()
    print(retHeader)
    for valueTuple in ret:
        for i in range(len(valueTuple)):
            print(str(varNames[i]) + "：" + str(valueTuple[i]) + "，", end="")
        print()

def registerToTable(tableName, pkDict, otherVarDict={}):
    """
    otherVarDict: 其他值的变量名和注册时说明，格式为：
        变量名: 变量在交互界面的输入说明
    """    
    condstr, colStr, valueStr = "", "", "'"
    for k in pkDict.keys():
        condstr += str(k) + " = '" + str(pkDict[k]) + "' AND "
        colStr += str(k) + ", "
        valueStr += str(pkDict[k]) + "', '"
    condstr += " TRUE "
    selector = Selector(tableName[0], condstr=condstr)
    ret = selector.returnRets()
    if len(ret) != 0:
        print("该拟注册或登记值在表中已存在！")
        return
    
    rowDict, timeDict = {}, {}
    for k, v in otherVarDict.items():
        rowDict[k] = input("请输入" + v + "：")        
        colStr += str(k) + ", "
        valueStr += rowDict[k] + "', '"
        if k == "startTime" or k == "finishTime":
            timeDict[k] = rowDict[k]
        
    if timeDict != {}:
        if not checkTimeLogic(timeDict["startTime"], timeDict["finishTime"]):
            print("您输入的起始时间早于终止时间，插入无效！请检查输入！")
            return
        
    colStr = colStr[:-2]
    valueStr = valueStr[:-len("', '")]
    valueStr += "'"
    adder = RowAdder(tableName[0], colStr, valueStr)
    ret = adder.writeInsertion()
    print(tableName[1] + "已成功注册!" if ret else "注册失败！")

def updateRowInTable(tableName, pkDict, newVarDict={}):
    """
    otherVarDict: 其他值的变量名和注册时说明，格式为：
        变量名: 变量在交互界面的输入说明
    """
    condstr = ""
    for k in pkDict.keys():
        condstr += str(k) + "='" + str(pkDict[k]) + "' AND "
        #valueStr += str(k) + "='" + str(pkDict[k]) + "', "
    condstr += " TRUE "
    selector = Selector(tableName, condstr=condstr)
    ret = selector.returnRets()
    if len(ret) == 0:
        print("该拟更新值还未注册，请先注册相应信息!")
        return
    
    rowDict, valueStr, timeDict = {}, "", {}
    for k, v in newVarDict.items():
        rowDict[k] = input("请输入新" + v + ": ")
        valueStr += str(k) + "='" + str(rowDict[k]) + "', "
        if k == "startTime" or k == "finishTime":
            timeDict[k] = rowDict[k]
        
    if timeDict != {}:
        if not checkTimeLogic(timeDict["startTime"], timeDict["finishTime"]):
            print("您输入的起始时间早于终止时间，插入无效！请检查输入！")
            return
        
    valueStr = valueStr[:-len("', ")]
    valueStr += "'"

    updater = RowUpdater(tableName, valueStr, condstr)
    ret = updater.writeUpdate()
    print("内容已成功更新!" if ret else "更新失败！")

def deregisterRowInTable(tableName, pkDict):
    condstr = ""
    for k in pkDict.keys():
        condstr += str(k) + "='" + str(pkDict[k]) + "' AND "
    condstr += " TRUE "
    selector = Selector(tableName, condstr=condstr)
    ret = selector.returnRets()
    if len(ret) == 0:
        print("该信息在系统中还未注册或已注销!")
        return
    deleter = Deleter(tableName, condstr)
    ret = deleter.writeDeletion()
    print("内容已成功删除!" if ret else "内容删除失败！")

class ClassManager:
    def __init__(self, tableName, pkColNames, otherColNames, tableHeader):
        """
        tableName - 二元组，（英文：中文)
        pkColNames - {英文原名：中文名}
        otherColNames - {英文原名：中文名}
        tableHeader - 中文，输出表格时的信息
        """
        self.tableName = tableName
        self.pkColNames, self.otherColNames = pkColNames, otherColNames
        self.tableHeader = tableHeader
        
    def formPkDict(self, update=False):
        pkDict = {}
        for colName in self.pkColNames.keys():
            if update:
                pkDict[colName] = input("请输入旧" + self.pkColNames[colName] + "：")
            else:
                pkDict[colName] = input("请输入" + self.pkColNames[colName] + "：")
        return pkDict
    
    def formVarNames(self):
        varNames = []
        for k in self.pkColNames.keys(): varNames.append(self.pkColNames[k])
        for k in self.otherColNames.keys(): varNames.append(self.otherColNames[k])
        return varNames
            
    def manageOperations(self):
        print("欢迎来到" + self.tableName[1] + "功能页面!")
        funcChoice = 0
        while funcChoice != 6:        
            try:
                funcChoice = int(
                    input("请输入1 - 查询特定" + self.tableName[1] + "信息，\n"
                    + "输入2 - 查看所有" + self.tableName[1] 
                        + "信息（注意此项操作可能会导致系统相应变慢），\n"
                    + "输入3 - 注册新" + self.tableName[1] + "信息，\n"
                    + "输入4 - 变更" + self.tableName[1] + "信息，\n"  
                    + "输入5 - 注销某一" + self.tableName[1] + "信息，\n"
                    + "输入6 - 退出本界面：".strip())
                )
                
                if funcChoice == 1:
                    checkTable(self.tableName[0], pkDict=self.formPkDict(), 
                               retHeader="查到的" + self.tableName[1] + "信息：", 
                               varNames=self.formVarNames())
                if funcChoice == 2:
                    checkTable(self.tableName[0], retHeader="查到的" + self.tableName[1] + "信息：",
                               varNames=self.formVarNames())
                if funcChoice == 3:
                    registerToTable(self.tableName, pkDict=self.formPkDict(), otherVarDict=self.otherColNames)
                if funcChoice == 4:
                    newVarDict = {}
                    newVarDict.update(self.pkColNames)
                    newVarDict.update(self.otherColNames)
                    updateRowInTable(self.tableName[0], pkDict=self.formPkDict(update=True), 
                            newVarDict=newVarDict)
                if funcChoice == 5:
                    deregisterRowInTable(self.tableName[0], pkDict=self.formPkDict())
            except ValueError:
                print("侦测到无效输入，请您重新输入！")


if __name__ == "__main__":
    """
    print(checkTimeLogic("2021-12-19 14:55:00", "2021-12-19 15:55:00")) # Return True
    print(checkTimeLogic("2021-12-19 15:55:00", "2021-12-19 14:55:00")) # Return False
    print(checkTimeLogic("2021-12-18 14:55:00", "2021-12-19 15:55:00")) # Return True
    print(checkTimeLogic("2021-12-19 15:55:00", "2021-12-18 14:55:00")) # Return False
    print(checkTimeLogic("2021-12-19 14:55:00", "2021-12-19 14:55:00")) # Return False
    """
    
    f = ClassManager(("customer", "客户"), {"customer_name":"客户姓名"}, 
        {"address":"客户地址", "phone":"客户电话", "email":"客户邮箱"}, 
        "以下为查到的客户信息：")
    f.manageOperations()