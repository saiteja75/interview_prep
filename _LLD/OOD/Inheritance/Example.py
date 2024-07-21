class Person:
    def __init__(self,name,gender) -> None:
        self.name = name
        self.gender = gender

    def getName(self):
        if self.gender == 'M':
            print('his name is '+ self.name)
        else:
            print('her name is '+ self.name)


class Student(Person):
    def __init__(self, name, gender, rollno) -> None:
        super().__init__(name, gender)
        self.rollno = rollno
    
    def getRollNo(self):
        return self.rollno
    

std1 = Student('sai','M','11')
std1.getName()
print(std1.getRollNo())