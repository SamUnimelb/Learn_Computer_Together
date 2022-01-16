# -*- coding: utf-8 -*-
"""
Created on Sun Jan 16 22:29:17 2022

@author: TR
"""

import sys
from ReaderPage import *
from PyQt5.QtWidgets import QApplication, QMainWindow

def private(*values):
    # python的严格封装方式，程序来自Mark Lutz。
    def controlPrivacy(cls):
        class PrivacyController:
            def __init__(self, *args, **kwargs):
                self.proxy = cls(*args, **kwargs)
            def __call__(self, cls, *args, **kwargs):
                return self.proxy
            def __getattr__(self, attr):
                print("Trying to get attr", attr)
                if attr in values:
                    raise AttributeError("Private variable unaccessible!")
                else: return getattr(self.proxy, attr)
            def __setattr__(self, attr, val):
                # Allow access inside the class
                if attr == 'proxy': self.__dict__[attr] = val
                elif attr in values:
                    raise AttributeError("Private variable unaccessible!")
                else: setattr(self.proxy, attr, val)
            def __str__(self):
                return self.proxy.__str__()
        return PrivacyController
    return controlPrivacy


@private("ui", "labelTxt")
class QMyWidget(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.labelTxt = "<html><head/><body><p align=\"center\"><span style=\" color:#ff0000;\">欢迎光临！</span></p></body></html>"
    
    def on_reader_pressed(self):
        #print(self.ui.label.text())
        #print(self.ui.label.text() == self.labelTxt)
        if self.ui.label.text() == self.labelTxt:
            self.ui.reader.setText("请出站刷卡")
            self.ui.label.setText(self.labelTxt.replace("欢迎光临！", "欢迎下次光临！"))
        else:
            self.ui.label.setText(self.labelTxt)
            self.ui.reader.setText("请进站刷卡")     
            

    
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myWidget = QMyWidget()
    myWidget.show()
    sys.exit(app.exec_())
    
