class BankAccount:
    def __init__ (self,int_rate,balance):
        self.int_rate = int_rate
        self.balance = 0
    def deposit(self,amount):
        self.balance += amount
        return self
    def withdraw(self,amount):
        if amount > self.balance:
            print ("insufficient funds:Charging a $5 fee")
        self.balance -= amount
        return self
    def display_account_info(self):
        print (("Balance:$"),self.balance,("Interest Rate:"),self.int_rate)
        if self.balance < 0:
            print(("Balance with fee :$"), self.balance - 5)
        return self
    def yeild_interest(self):
        print (("Interest Yielded:$"),self.balance * self.int_rate)
        print(("New Balance:$"), (self.balance*self.int_rate)+self.balance)
        return self

BankAccount1 = BankAccount(.02,0)
BankAccount2 = BankAccount(.04,0)

BankAccount1.deposit(100).deposit(250).deposit(50).withdraw(200).yeild_interest().display_account_info()
BankAccount2.deposit(250).deposit(25).withdraw(100).withdraw(15).withdraw(100).withdraw(1).yeild_interest().display_account_info()