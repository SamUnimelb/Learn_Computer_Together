# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 17:34:48 2022

@author: TR
"""

def writeLog(logStr):
    with open("logger.txt", "a") as f:
        f.write(logStr + "\n")  
    
class BankAccount:
    
    def __init__(self, account, amount):
        self.__account, self.__amount = account, amount
        
    def getAccountID(self):
       return self.__account
        
    def getAmount(self):
        writeLog(self.__account + " checked balance!")
        return self.__amount
    
    def deposit(self, howMuch):
        self.__amount += howMuch
        writeLog(self.__account + " deposited " + str(howMuch) + ".")
    
    def takeMoney(self, howMuch:float):
        if howMuch > 1000:
            print("Too much! Please go to counter to take this!")
            writeLog(self.__account + " tried to take money but failed.")
            return
        self.__amount -= howMuch;
        print(str(howMuch) + " took from your account!");
        writeLog(str(howMuch) + " took from " + self.__account + "!");

class Person:
    
    def __init__(self, name:str, bankAccount:BankAccount):
        self.__name = name
        self.__bankAccount = BankAccount(bankAccount.getAccountID(), 
                bankAccount.getAmount())
    
    def getAccount(self):
        return self.__bankAccount;

 
if __name__ == "__main__":
       account1 = BankAccount("5247123434566789", 10000);
       samY = Person("Sam Yan", account1);
       hacker = Person("Hacker", account1);
       for i in range(10):
           hacker.getAccount().takeMoney(500);
       print("Remained amount in Sam: " + str(samY.getAccount().getAmount()));
    
 
    