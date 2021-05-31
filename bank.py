from datetime import datetime
class BankAccount:
    fixedAccount="fixed"
    savingsAccount="save"
    def __init__(self,name,phonenumber):
        self.name=name
        self.phonenumber=phonenumber
        self.balance=0
        self.loan=0
        self.statement=[]#instasiating statement as an empty list so we can add values

    def withdraw(self):
        return f"please confirm your withdrawal from account {self.name}"
    def show_balance(self):
        return f" Hello {self.name} your balance is {self.balance}"
    def deposit(self,amount):
        if amount<=0:
            return f"you cannot deposit less than 0"
        else:
             self.balance+=amount
             now=datetime.now()
             transaction={"amount":{amount},"time":now,"narration":"you have deposited"}#a dictionary with transaction details
             self.statement.append(transaction)#appending transactions in the empty list statements
        return self.show_balance()

    def show_statement(self):
        for transaction in self.statement:
            amount=transaction["amount"]
            narration=transaction["narration"]
            time=transaction["time"]
            date=time.strftime("%d/%m/%y")
            print(f"{date}:{narration} {amount}")
        return  
    def withdraw(self,amount):
        if amount>self.balance:
            return f"your balance is {self.balance} you cannot withdraw{amount}"
        else:
            self.balance-=amount
            now=datetime.now()
            withdrawals={"amount":{amount},"time":now,"narration":"you have withdrawn"}#a dictionary with transaction details
            self.statement.append(withdrawals)
        return self.show_balance()

    def borrow(self,amount):
        return f"congragulations you can borrow ksh{amount}"

    def repayloan(self,amount):
            return f"you have repaid your loan of ksh{amount}"


    


        


    