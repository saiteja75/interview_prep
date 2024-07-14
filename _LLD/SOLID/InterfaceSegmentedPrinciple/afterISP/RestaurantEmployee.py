from abc import abstractmethod,ABC

# This is abstract class for a waiter
class WaiterInferace(ABC):

    @abstractmethod
    def serveCustomer():
        pass

    @abstractmethod
    def takeOrder():
        pass

# this is abstract class for chef
class ChefInterface(ABC):

    @abstractmethod
    def cookFood():
        pass

    @abstractmethod
    def decideMenu():
        pass

# This is waiter class
# This is not voilationg the interface segment principle
class Waiter(WaiterInferace):
    def __init__(self) -> None:
        super().__init__()
    

    def serveCustomer():
        print('waiter is serving the customer')

    def takeOrder():
        print('waiter is taking order')