

# Class
class Car:
    def __init__(self,make,model,year) -> None:
        self.make = make
        self.model = model
        self.year = year

    def drive(self):
        print('driving '+self.model+' car.')


# Object
carObj = Car('Maruti','Deszire',2020)