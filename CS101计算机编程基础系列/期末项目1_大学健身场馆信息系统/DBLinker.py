# -*- coding: utf-8 -*-
"""
Created on Sun Dec 19 07:25:07 2021
@author: Sam Yan
如果老师不让用数据库，这些代码先替换为特定文件的增一行、删一行以及读取特定内容，
然后更新的过程为先删掉查到的信息，再写入新的信息。
"""

import mysql.connector as connector

config={'host':'127.0.0.1', # 数据库系统所在IP
        'user':'root', # 数据库系统用户名，默认为root 
        'password':'Sams_MySQL_56_Server',
        'port':3306, # 服务器数据库监听端口 
        'database':'gym_sys', # 本系统所用的数据库名
        'charset':'utf8'}

def executeQuery(query, isSelecting=False):
    #print(query)
    querySuccess = True
    try:
        cnn = connector.connect(**config)
        cursor = cnn.cursor()
        cursor.execute(query)
        
        if isSelecting:
            ret = cursor.fetchall()
        cnn.commit()
    except connector.Error as e:
        print(e)
        print("Query falsely executed.")
        querySuccess = False
    finally:
        cursor.close()
        cnn.close()
        
    if isSelecting: return ret
    return querySuccess
    

class RowAdder:    
    def __init__(self, tableName, colNamestr, valuestr):
        self.tableName = tableName
        self.colNamestr = colNamestr
        self.valuestr = valuestr        
    
    def writeInsertion(self):
        query = ("INSERT INTO " + self.tableName + " (" + self.colNamestr
             + ") " + " VALUES (" + self.valuestr + ");")
        #print(query)
        return executeQuery(query)
        
class RowUpdater: 
    """Another solution is you don't write updater but only adder and deleter,
    and then perform deletion with a condition and then insert again.
    But this suffers your DB speed when it grows. """
    def __init__(self, tableName, setstr, condstr):
        self.tableName = tableName
        self.setstr = setstr
        self.condstr = condstr
    def writeUpdate(self):
        query = ("UPDATE " + self.tableName + " SET " + self.setstr + 
                 " WHERE " + self.condstr + ";")
        #print(query)
        return executeQuery(query)


class Deleter:
    def __init__(self, tableName, condstr):
        self.tableName = tableName
        self.condstr = condstr
    def writeDeletion(self):
        query = "DELETE FROM " + self.tableName + " WHERE " + self.condstr + ";"
        #print(query)
        return executeQuery(query)
        
class Selector:
    def __init__(self, tablestrs, colNamestr="*", condstr="TRUE"):
        #"""tablestrs support things like t1 INNER JOIN t2 ON t1.k = t2.k""""
        self.tablestrs = tablestrs
        self.colNamestr = colNamestr
        self.condstr = condstr
    def returnRets(self):
        query = ("SELECT " + self.colNamestr + " FROM " + 
                 self.tablestrs + " WHERE " + self.condstr + ";")
        #print(query)
        ret = executeQuery(query, True)
        return ret
        
if __name__ == "__main__":
    # Test insertion:
    adder = RowAdder("customer", "customer_name, address, phone, email",
                     "'Mohamed Ahmed','1 WKU st', '13858242525', 'mhahaha@wku.edu.cn'")
    adder.writeInsertion()
    adder = RowAdder("customer", "customer_name, address, phone, email",
                     "'Ahmed','2 WKU st', '13858242535', 'mhehe@wku.edu.cn'")
    adder.writeInsertion()

    updater = RowUpdater("customer", "customer_name='Relic', "
                         + "address='13 WKU st', email='wangyf@kean.edu'", 
                         "customer_name='Ahmed'")
    updater.writeUpdate()

    deleter = Deleter("customer", "customer_name='Relic'")
    deleter.writeDeletion()

    
    adder = RowAdder("gym_hall", "hall_name", "'葛和凯楼'")
    adder.writeInsertion()
    adder = RowAdder("gym_hall", "hall_name", "'陈天龙美术馆'")
    adder.writeInsertion()
    adder = RowAdder("gym_hall", "hall_name", "'王永富的教室'")
    adder.writeInsertion()
    
    selector = Selector("customer")
    ret = selector.returnRets()
    print(ret)
    print(len(ret))
    
    selector = Selector("gym_hall")
    ret = selector.returnRets()
    print(ret)
    print(len(ret))