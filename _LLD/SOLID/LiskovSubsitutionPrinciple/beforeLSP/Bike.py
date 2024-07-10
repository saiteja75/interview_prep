'''
This code demonstrates the voliation of Liskav Subsititution Principle

'''

from abc import ABC, abstractmethod


# interface for the motorcycle and cycle classes
class Bike(ABC):
    
    @abstractmethod
    def turnOnEngine():
        pass

    @abstractmethod
    def accelerate():
        pass


# This class is following LSP principle because it is extending the base class method functionality so this
# is not breaking the existing behavior and can be replacible
class MotorCycle(Bike):
    def __init__(self, model,maxspeed,currspeed) -> None:
        super().__init__()
        self.model = model
        self.maxspeed = maxspeed
        self.currspeed = currspeed

    def turnOnEngine(self):
        print('Enginee turned on')

    def accelerate(self):
        self.currspeed += 10


# This class is voliating the LSP because it is breaking the existing functionality of the base class not extending
# and it is no more replacible for base class
class Cycle(Bike):
    def __init__(self,currspeed) -> None:
        super().__init__()
        self.currspeed = currspeed

    def turnOnEngine():
        raise Exception('Cycle does not have engine')
    
    def accelerate(self):
        self.currspeed+=5