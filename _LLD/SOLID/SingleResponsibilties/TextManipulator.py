'''
Example 1: We need to develop a Feature where we can manipulate a given text in different ways and Print the text in different ways
Solutions:  This feature can be developed in many ways, mentioning some below:
1.	Developing both the features in a single place
2.	Break Down the Feature into multiple parts where each part does one job
•	One Class does the job of Text Manipulating
•	One Cass does the job of Print the text
'''

# Developing both the features in a single place
class TextManipulator:
    def __init__(self,text) -> None:
        self.text = text

    def getText(self):
        return self.text
    
    def appendText(self,value):
        self.text += value
    
    def replaceText(self,value,newValue):
        if (value in self.text):
            self.text = self.text.replace(value,newValue)
    
    def printText(self):
        print(self.text)


# Break Down the Feature into multiple parts where each part does one job
class TextManipulator:
    def __init__(self,text) -> None:
        self.text = text

    def getText(self):
        return self.text
    
    def appendText(self,value):
        self.text += value
    
    def replaceText(self,value,newValue):
        if (value in self.text):
            self.text = self.text.replace(value,newValue)
    
class Printer:
    def __init__(self,textManipulator) -> None:
        self.textManipulator = textManipulator

    def printText(self):
        print(self.textManipulator.getText())
