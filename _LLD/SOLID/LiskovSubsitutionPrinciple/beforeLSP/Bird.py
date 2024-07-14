from abc import ABC,abstractmethod 

# Abstract class for the birds, This is parent class
class Bird(ABC):
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def fly():
        pass

    @abstractmethod
    def eat():
        pass

# Child class Eagle which is inheriting the methods of Bird class
# According to liskov subitution principle: Eagle class can be subsituted as parent class because
# it is not breaking the behavior
class Eagle(Bird):
    def __init__(self) -> None:
        super().__init__()
    
    def fly():
        print('Eagle is flying')
    
    def eat():
        print('Eagle is eating')

# Child class Penguin which is inheriting the methods of Bird class
# According to liskov subitution principle: Penguin class cannot be subsituted as parent class because
# it is breaking the behavior of fly method
class Penguin(Bird):
    def __init__(self) -> None:
        super().__init__()
    
    def fly():
        raise Exception('Penguin cannot fly')
    
    def eat():
        print('Penguin is eating')


eagle =  Eagle()
penguin = Penguin()


