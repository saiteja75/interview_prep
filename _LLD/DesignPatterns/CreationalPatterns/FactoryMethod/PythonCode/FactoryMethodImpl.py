from abc import ABC, abstractmethod

# Super Class
class FactoryClass(ABC):
   def __init__(self) -> None:
      super().__init__()
      pass

   # This method will be overwritten/alter by the child class
   @abstractmethod
   def genericMethod():
      pass


# Child Class 1
class ChildOne(FactoryClass):
   def __init__(self) -> None:
      super().__init__()

   def genericMethod():
      print("this is method in child class1")

# Child Class 2
class ChildTwo(FactoryClass):
   def __init__(self) -> None:
      super().__init__()

   def genericMethod():
      print('this is method in child class2')