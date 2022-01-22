# -*- coding: utf-8 -*-
"""
Created on Sat Jan 22 11:23:58 2022

@author: TR
"""

import sys
from FontDemo import *
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPalette
from PyQt5.QtCore import Qt, pyqtSlot

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
class QMyWidget(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # 关联单选按钮
        self.ui.black.clicked.connect(self.setTextColor)
        self.ui.blue.clicked.connect(self.setTextColor)
        self.ui.red.clicked.connect(self.setTextColor)
        
    @pyqtSlot(bool)
    def on_bold_clicked(self, checked):
        font = self.ui.textEdit.font()
        font.setBold(checked)
        self.ui.textEdit.setFont(font)
        
    @pyqtSlot(bool)
    def on_italic_clicked(self, checked):
        font = self.ui.textEdit.font()
        font.setItalic(checked)
        self.ui.textEdit.setFont(font)
        
    @pyqtSlot(bool)
    def on_underline_clicked(self, checked):
        font = self.ui.textEdit.font()
        font.setUnderline(checked)
        self.ui.textEdit.setFont(font)
        
    def setTextColor(self):
        palette = self.ui.textEdit.palette()
        if self.ui.blue.isChecked():
            palette.setColor(QPalette.Text, Qt.blue)
        elif self.ui.red.isChecked():
            palette.setColor(QPalette.Text, Qt.red)
        else:
            palette.setColor(QPalette.Text, Qt.black)
        self.ui.textEdit.setPalette(palette)
            

    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWidget = QMyWidget()
    myWidget.show()
    sys.exit(app.exec_())
    