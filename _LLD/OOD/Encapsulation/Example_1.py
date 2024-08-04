from datetime import datetime
class Person:
    def __init__(self,name,YOB,salary) -> None:
        # public access modifiers
        self.name = name
        self.YOB = YOB
        # protected access modifiers
        self._age = datetime.now().year - YOB
        # private access modifiers
        self.__salary = salary


pr1 = Person('sai',1998,1234)
print(pr1.name)
print('get',pr1._age)
pr1._age = 97
print('get', pr1._age)
print(pr1.__salary)

        