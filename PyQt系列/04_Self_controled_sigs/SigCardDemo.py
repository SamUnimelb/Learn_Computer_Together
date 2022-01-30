# -*- coding: utf-8 -*-
"""
Created on Sun Jan 30 09:53:19 2022
@author: TR
"""

from PyQt5.QtCore import QObject, pyqtSlot, pyqtSignal

class Uploader(QObject): # 前端UP主对象代码
    fansChanged = pyqtSignal(int)
    userNameChanged = pyqtSignal([str, str], [str, int])
    
    def __init__(self, userName, bankAcc=None, points=0, fans=1, parent=None):
        super().__init__(parent)
        self.userName = userName
        self.bankAcc = bankAcc
        self.points = points
        self.fans = fans    
    
    def follow(self):
        print("恭喜up，有新粉丝关注啦！")
        self.fans += 1
        self.fansChanged.emit(self.fans)
        
    def unFollow(self):
        print("哎，又掉粉了。。。")
        self.fans -= 1
        self.fansChanged.emit(self.fans)
    
    def setNewUserNameBank(self, newName, bank):
        self.userName = newName
        self.bankAcc = bank
        self.userNameChanged[str, str].emit(self.userName, self.bankAcc)
        
    def setNewUserNamePoint(self, newName, pointsRemained):
        self.userName = newName
        if pointsRemained - 6 >= 0:
            self.points = pointsRemained - 6
            self.userNameChanged[str, int].emit(self.userName, self.points)
        else:
            raise ValueError("点数用光啦，请充值！")


class BackEnd(QObject):
    #@pyqtSlot(str, str)
    def changeUserName(self, newName, bankCard):
        print("您的新用户名是： ", newName)
        print("6元改用户名费已成功从", bankCard, "扣除！")
        
    def changeUserNameByPoints(self, newName, pointsRemained):
        print("您的新用户名是： ", newName)
        print("剩余点数：", pointsRemained)
    
    @pyqtSlot(int) # 可写可不写
    def printFansNum(self, fansNum):
        print("当前粉丝数为：", fansNum)
        

if __name__ == "__main__": # 界面代码
    up = Uploader("自然研究者")
    bk = BackEnd()
    
    up.fansChanged.connect(bk.printFansNum)
    for i in range(5):
        up.follow()
    up.unFollow()
    
    
    up.userNameChanged[str, str].connect(bk.changeUserName)  
    up.setNewUserNameBank("自然研究者", "1234567832144052")
    
    up.userNameChanged[str, int].connect(bk.changeUserNameByPoints)  
    up.setNewUserNamePoint("自燃研究者", 18)
    