class BankAccount:
    fixedAccount="fixed"
    savingsAccount="save"
    def __init__(self,pin,balance):
        self.pin=pin
        self.balance=balance
    def withdraw(self):
        return f"please confirm your withdrawal from account {self.pin}"
    def deposit(self):
        return f"your deposit of ksh 1200 has been received and your balance is {self.balance}"
    