# -*- coding: utf-8 -*-
"""
Created on Sun Jan 16 17:28:16 2022
@author: Sam
@ref: 王维波等所著书本《Python Qt GUI与数据可视化编程》
"""
import sys
from HelloDialog import *

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


@private("ui")
class QMyWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        #self.labelTxt = "自定义的标签"
        #self.ui.helloLabel.setText(self.labelTxt)
    
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myWidget = QMyWidget()
    #myWidget.setBtnText("我自定义的按钮")
    myWidget.show()
    try:
        print(myWidget.ui)
    except AttributeError as e:
        print(e)
    sys.exit(app.exec_())
    
