# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 17:17:44 2022
@author: Sam Yan
"""

import sys
from NewYearGUI import *
from PyQt5.QtWidgets import QApplication, QMainWindow
import random

class QMyWidget(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.templateTxt = "<html><head/><body><p><span style=\" color:#ff0000;\">新年快乐！</span></p></body></html>"
        self.currTxt = "新年快乐！"
        self.wishTxts = ["虎年吉祥！", "虎虎生威！", "阖家幸福！", "安康美满！", 
                         "工作顺利！", "万事胜意！", "一键三连！"]
        
    def on_pushButton_pressed(self):
        newTxt = random.choice(self.wishTxts)
        self.templateTxt = self.templateTxt.replace(self.currTxt, newTxt)
        self.ui.label.setText(self.templateTxt)
        self.currTxt = newTxt
    
     
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWidget = QMyWidget()
    myWidget.show()
    sys.exit(app.exec_())