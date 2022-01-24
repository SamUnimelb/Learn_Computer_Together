# -*- coding: utf-8 -*-
"""
Created on Sun Dec 19 15:49:03 2021
@author: Sam Yan
本实现方案实际用时约10小时，使用其他编程语言如Java或C++等应在此基础上适度花费更多
实现和调试时间。
"""

from EntityManager import ClassManager

class GymHall:
    def __init__(self):
        self.mgr = ClassManager(("gym_hall", "场馆"), {"hall_name":"场馆名称"},
                                {}, "以下为查到的场馆信息：")
        self.mgr.manageOperations()

class Customer:
    def __init__(self):
        self.mgr = ClassManager(("customer", "客户"), {"customer_name":"客户姓名"},
                {"address":"客户地址", "phone":"客户手机号", "email":"客户邮箱"}, 
                "以下为查到的客户信息：")
        self.mgr.manageOperations()

class Equipment:
    def __init__(self):
        self.mgr = ClassManager(("equipment", "器材"), {"equip_seq_num":"器材序列号或名称"},
                {"hall_name":"所在场馆", "equipment_description":"器材描述"}, 
                "以下为查到的客户信息：")
        self.mgr.manageOperations()
        
class Trainer:
    def __init__(self):
        self.mgr = ClassManager(("trainer", "教练"), {"trainer_name":"教练姓名"},
                {"hall_name":"所在场馆"}, 
                "以下为查到的教练信息：")
        self.mgr.manageOperations()
        
class OpenHRs:
    def __init__(self):
        self.mgr = ClassManager(("openhrs", "场馆开放时间"), 
                {"hall_name":"场馆名称", "weekday":"周几（整数数值）开放"},
                {"startTime":"开始开放时间", "endTime":"结束开放时间"}, 
                "以下为查到的场馆开放信息：")
        self.mgr.manageOperations()

class ExercisePlans:
    def __init__(self):
        self.mgr = ClassManager(("exercise_plan", "训练计划"), 
                {"idexercise_plan":"计划书号"},
                {"trainer_name":"教练姓名", "plandetails":"训练细节"}, 
                "以下为查到的训练计划书信息：")
        self.mgr.manageOperations()
        print()
        self.assigns = Assign()
        # 不要执行下一行，否则器材使用计划会跳出来两遍：
        # self.assigns.mgr.manageOperations()

class Assign:
    def __init__(self):
        self.mgr = ClassManager(("assign", "器材使用计划"), 
                {"idexercise_plan":"计划书号", "idequipment":"器材序列号或名称",
                 "equip_seq_num":"本次训练中该器材的顺序号"},
                {"duration":"预计器材持续使用时间"}, 
                "以下为查到的训练过程器材使用计划信息：")
        self.mgr.manageOperations()

class Subscribe:
    def __init__(self):
        self.mgr = ClassManager(("subscribe", "客户教练分配情况"), 
                    {"customer_name":"客户姓名", 
                     "meetingTime":"会面时间（格式：YYYY-MM-DD HH:MM:SS）"}, 
                    {"trainer_name":"教练姓名"},
                    "以下为查询到的客户教练分配情况：")
        self.mgr.manageOperations()

class Follow:
    def __init__(self):
        self.mgr = ClassManager(("follow", "客户拟执行训练计划书情况"), 
            {"customer_name":"客户姓名", "exercise_plan":"计划书号"},
            {"startTime":"计划开始时间", "finishTime":"计划结束时间"}, 
             "以下为查到的客户拟执行训练计划书情况：")
        self.mgr.manageOperations()

if __name__ == "__main__":
    funcDict = {1:GymHall, 2:Customer, 3:Equipment, 4:Trainer,
                5:OpenHRs, 6:ExercisePlans, 7:Subscribe, 8:Follow}
    print("欢迎来到校健身场馆管理系统！")
    funcChoice = 0
    while funcChoice != 9:    
        try:
            funcChoice = int(input("""请输入对应数字进入相应管理页面: 
1 - 管理场馆信息，
2 - 管理客户信息，
3 - 管理器材信息，
4 - 管理教练信息，
5 - 管理场馆开放信息，
6 - 管理训练计划信息，
7 - 管理客户教练分配信息，
8 - 管理客户训练计划信息，
9 - 退出系统："""))
            funcDict[funcChoice]()
        except ValueError:
            print("侦测到无效输入，请您重新输入！")
        except KeyError:
            if funcChoice != 9:print("侦测到无效输入，请您重新输入！")
                
    
        
    
    


    
    
