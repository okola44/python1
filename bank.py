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
        try:
            10+amount
        except TypeError:
            return f"the amount should be an integer"
        


        if amount<=0:
            return f"you cannot deposit less than 0"
        else:
             self.balance+=amount
             now=datetime.now()
             transaction={"amount":amount,"time":now,"narration":"you have deposited"}#a dictionary with transaction details
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
        try:
            30-amount
        except TypeError:
            return f"amount should be an integer"
        if amount>self.balance:
            return f"your balance is {self.balance} you cannot withdraw{amount}"
        else:
            self.balance-=amount
            now=datetime.now()
            withdrawals={"amount":amount,"time":now,"narration":"you have withdrawn"}#a dictionary with transaction details
            self.statement.append(withdrawals)
        return self.show_balance()

    def borrow(self,amount):
        try:
            20+amount
        except TypeError:
            return f"amount should be in figures"
        if amount <0:
            return f"you cannot borrow a negative amount"
        elif self.loan>0:
            return f"you cannot borrow an amount of {amount}"
        elif amount>0.1*self.balance:
            return f" you do not qualify for the loan of ksh {amount}"
        else:
            loan=amount*1.05
            self.loan=loan
            self.balance+=amount
            now=datetime.now()
            borrow_transaction={"amount":amount,"time":now,"narration":"you have borrowed ksh"}
            self.statement.append(borrow_transaction)
            return f"your outstanding loan is ksh {self.loan}"

    def repay_loan(self,amount):
        try:
            20-amount
        except TypeError:
            return f"amount should be in figures"
        if amount<0:
            return "you cannot repay with a negative amount"
        elif amount<=self.loan:
            loan_balance=self.loan-amount
            return f"you have paid ksh{amount} your outstanding loan balance is {loan_balance} "
        else:
             
            excess=amount-self.loan
            self.loan=0
            self.deposit(excess)
            now=datetime.now()
            repay_transaction={"amount":amount,"time":now,"narration":"you have repaid your loan of ksh"}
            self.statement.append(repay_transaction)
            return f"you have fully repaid your loan and your excess of ksh {excess} has been deposited in your account,your balance is {self.balance} "
    
    def transfer(self,account,amount):
        try:
            20-amount
        except TypeError:
            return f"amount should be in figures"
        fee=amount*0.05
        total=amount+fee
        if amount<0:
            return f"you have cannot transfer a negative number"
        elif total>self.balance:
            return f"you do not have enough money to transfer ksh{amount} you need at least ksh{total}"
        else:
            self.balance-=total
            account.deposit(amount)

class mobile_moneyAccount(BankAccount):
    def __init__(self, name, phonenumber,service_provider):
        
        BankAccount.__init__(self,name, phonenumber)
        self.service_provider=service_provider
        

    def buy_airtime(self,amount):
        try:
            30*amount
        except TypeError:
            return f"amount must be in figures"
        if amount<0:
            return f"amount must be greaer than 0 and not a negateive figure"
        elif self.balance<amount:
            return f" dear customer,your balance is {self.balance} you cannot purchase airtime worth {amount} "
        else:
            self.balance-=amount
            
               

      


            


            

        
    
    


    


        


    