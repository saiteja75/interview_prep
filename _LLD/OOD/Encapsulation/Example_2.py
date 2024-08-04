

class BankAccount():
    def __init__(self, Account_Number, balance) -> None:
        self.__Account_Number = Account_Number
        self.__balance = balance
    

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self,amount):
        if amount > self.__balance:
            print('Insufficient Balance')
        else:
            self.__balance -= amount
            print('WithDrawal Successful')
    
    def get_balance(self):
        return self.__balance

bankAccObj = BankAccount('1123458910', 200)
bankAccObj.get_balance()