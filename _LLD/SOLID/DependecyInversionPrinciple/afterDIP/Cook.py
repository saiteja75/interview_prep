
from abc import ABC,abstractmethod
class Bakable(ABC):
    @abstractmethod
    def bake():
        pass 

class Bread(Bakable):
    def bake():
        print('bread is baking')
    
class Cookie(Bakable):
    def bake():
        print('cookie is baking')


# Cook is not voilating the DIP
def cook(bakable: Bakable):
    bakable.bake()

bread = Bread()
cookie = Cookie()
cook(bread)
cook(cookie)


