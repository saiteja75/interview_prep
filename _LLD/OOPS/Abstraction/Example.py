from abc import ABC, abstractmethod

class Demo(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def method1(self):
        print('This is abstract method')
        pass


    def method2(self):
        pass

class Child(Demo):
    def __init__(self):
        pass

    def method1(self):
        super().method1()
        print('this is child method')
        pass


# Throws Error because its a abstract class
#demoObj = Demo()
    
childObj = Child()
childObj.method1()
