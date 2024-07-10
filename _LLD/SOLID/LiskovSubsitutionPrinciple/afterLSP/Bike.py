'''
This code demonstrates use of Liskav Subsititution Principle

'''

from abc import ABC, abstractmethod


# interface for the motorcycle and cycle classes
class Bike():

    def accelerate():
        pass

# creating a separate interface or class which is not common for sub classes and adding this class or interface
# to require sub-classes
class Engine(ABC):
    @abstractmethod
    def turnOnEngine():
        pass


# This class is following LSP principle because it is extending the base class method functionality so this
# is not breaking the existing behavior and can be replacible
class MotorCycle(Bike,Engine):
    def __init__(self, model,maxspeed,currspeed) -> None:
        super().__init__()
        self.model = model
        self.maxspeed = maxspeed
        self.currspeed = currspeed

    def turnOnEngine(self):
        print('Enginee turned on')

    def accelerate(self):
        self.currspeed += 10


# This class is following LSP principle because it is extending the base class method functionality so this
# is not breaking the existing behavior and can be replacible
class Cycle(Bike):
    def __init__(self,currspeed) -> None:
        super().__init__()
        self.currspeed = currspeed
    
    def accelerate(self):
        self.currspeed+=5
