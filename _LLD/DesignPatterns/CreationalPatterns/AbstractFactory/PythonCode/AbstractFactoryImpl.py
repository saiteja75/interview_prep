from abc import ABC,abstractmethod

# Abstract Classes
class IButton():

   @abstractmethod
   def click():
      pass

class ITextBox():

   @abstractmethod
   def showText():
      pass

class WINButton(IButton):

   def __init__(self) -> None:
      super().__init__()
      print('WINButton initialized')

   def click(self):
      print('WINDOWS BUTTON CLICKED')

class MACButton(IButton):
   def __init__(self) -> None:
      super().__init__()
      print('MACButton initialized')

   def click(self):
      print('MAC BUTTON CLICKED')


class WINTextBox(ITextBox):

   def __init__(self) -> None:
      super().__init__()
      print('WINTextBox initialized')

   def showText(self):
      print('WINDOWS TextBox text showed')

class MACTextBox(ITextBox):
   def __init__(self) -> None:
      super().__init__()
      print('MACTextBox initialized')

   def click(self):
      print('MAC Textbox text showed')

class IFactory(ABC):
   @abstractmethod
   def createButton(self):
      pass

   @abstractmethod
   def createTextbox(self):
      pass

class WINFactory(IFactory):

   
   def createButton(self):
      return WINButton()
   
   def createTextbox(self):
      return WINTextBox()

class MACFactory(IFactory):

   
   def createButton(self):
      return MACButton()
   
   def createTextbox(self):
      return MACTextBox()

class GUIFactory(ABC):
   
   @abstractmethod
   def createFactory(self, osType) -> IFactory:
      factory = None
      if(osType == 'WIN'):
         factory = WINFactory() 
      elif(osType == 'MAC'):
         factory = MACFactory()

      return factory


# Client Code
if __name__ == '__main__':
   print('Enter OS Type:')
   osType = input()
   factory = GUIFactory.createFactory(osType)
   button = factory.createButton()
   button.press()
   textbox = factory.createTextBox()
   textbox.showText()
