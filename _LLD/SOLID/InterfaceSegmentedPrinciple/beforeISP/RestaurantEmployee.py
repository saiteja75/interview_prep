from abc import abstractmethod,ABC

# This is abstract class for a employee in a restaurant
class RestaurantEmployee(ABC):
    @abstractmethod
    def cookFood():
        pass

    @abstractmethod
    def serveCustomer():
        pass

    @abstractmethod
    def washDishes():
        pass

# This is waiter class
# As you can see Waiter job is not cookFood or wash dishes but still we forcing the Waiter(client)
# to implement those even though it is not required
class Waiter(RestaurantEmployee):
    def __init__(self) -> None:
        super().__init__()
    
    def cookFood():
        pass

    def serveCustomer():
        print('waiter is serving the customer')

    def washDishes():
        pass