
class Person:
    def __init__(self, name):
        self.__name = name

    def getName(self):
        return self.__name
    
if __name__ == "__main__":
    jason = Person("Jason")
    print("Welcome,", jason.getName() + "!")