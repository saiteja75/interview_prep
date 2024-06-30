'''
Given Existing FootBaller Class which print the name of the footballer with his role as one of the method.
Support new roles after refactor the code to follow open/closed principle

'''

from abc import ABC, abstractmethod

# Existing Code:
class FootBaller:
    def __init__(self,name,age,role) -> None:
        self.name = name
        self.age = age
        self.role = role

    
    def getFootballerRole(self):
        role = self.role

        if(role == 'GoalKeeper'):
            print(self.name + 'is a goalkeeper')
        elif(role == 'Defender'):
            print(self.name+'is a defender')


# Refactored Code with new role support
class FootBaller:
    def __init__(self,name,age,role) -> None:
        self.name = name
        self.age = age
        self.role = role
    
    def getFootballerRole(self):
        return self.role.getRole()

class PlayerRole(ABC):
    @abstractmethod
    def getRole():
        pass


class GoalKeeper(PlayerRole):
    def getRole():
        return 'GoalKeeper'

class Defender(PlayerRole):
    def getRole():
        return 'Defender'
    
class Attacker(PlayerRole):
    def getRole():
        return 'Attacker'
    
