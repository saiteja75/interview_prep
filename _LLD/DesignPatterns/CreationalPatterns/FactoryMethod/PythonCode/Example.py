from abc import ABC,abstractmethod

class Button(ABC):
   def __init__(self) -> None:
      super().__init__()
   
   @abstractmethod
   def render():
      pass

   @abstractmethod
   def click():
      pass

class WindowsButton(Button):
   def __init__(self,width,height) -> None:
      super().__init__()
      self.width = width
      self.height = height

   def render(self):
      print('rendering the windows button in windows style')

   
   def onClick(self, func):
      print('Bind with Native OS click and trigger function')

class MACButton(Button):
   def __init__(self,width,height) -> None:
      super().__init__()
      self.width = width
      self.height = height

   def render(self):
      print('rendering the Mac button in Apple style')

   
   def onClick(self, func):
      print('Bind with Native Apple OS click and trigger function')


class Dialog:
   def __init__(self) -> None:
      pass

   def render(self):
      okButton = self.createButton()
      okButton.render()

   def createButton(self):
      pass

class WindowsDialog(Dialog):
   def __init__(self) -> None:
      pass

   def createButton(self):
      return WindowsButton(100,200)
   

class MACDialog(Dialog):
   def __init__(self) -> None:
      pass

   def createButton(self):
      return MACButton(100,200)


class App:
   dialog = None

   def __init__(self) -> None:
      pass

   def createDialog(self,type):
      if type == 'WINDOWS':
         self.dialog = WindowsDialog()
      elif type == 'MAC':
         self.dialog = MACDialog()
      else:
         raise Exception('Please provide type')







   