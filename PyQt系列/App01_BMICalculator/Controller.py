# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 08:32:13 2023

@author: Sam_Yan
"""

import sys
from Calculator import *
from PyQt5.QtWidgets import QApplication, QMainWindow

def private(*values):
    # Encapsulation of variables, from Mark Lutz。
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

def getSuggestion(BMIValue):
    if BMIValue < 18.4:
        return "You are underweight, \nmay want to eat more!"
    elif BMIValue < 25:
        return "Normal range, keep healthy!"
    return "You are overweight, \nmay want to exercise \nmore and eat less!"

@private("ui", "labelTxt")
class QMyWidget(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
    
    def on_pushButton_pressed(self):
        # For students to deal with:
        height = float(self.ui.heightValue.text()) / 100
        weight = float(self.ui.weightValue.text())
        BMIValue = weight / (height ** 2)
        
        # For teacher to deal with:
        self.ui.valueLabel.setText("Your BMI: " + str(round(BMIValue, 2)))
        self.ui.suggestion.setText(getSuggestion(BMIValue))
        self.ui.suggestion.adjustSize()
            
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWidget = QMyWidget()
    myWidget.show()
    sys.exit(app.exec_())