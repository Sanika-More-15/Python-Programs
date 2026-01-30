class BankAcount:
    ROI=10.5

    def __init__(self,):
        self.Name=input("Enter Name :")
        self.Amount=int(input("Enter nay amount :"))
        

    def Display(self):
        print("Acount Holder Name is :",self.Name)
        print("Current Balance :",self.Amount)

    def Deposit(self):
        amt=int(input("Enter amount for Deposit:"))
        self.Amount=self.Amount + amt
        print("Updated Balance is :",self.Amount)

    def Withdraw(self):
        withd=int(input("Enter amount for Withdrawal :"))
        if withd <= self.Amount:
            self.Amount = self.Amount -withd
            print("Updated balance is :",self.Amount)
        else:
            print("Insufficient Balance")

    def CalculateInterest(self):
        Interest=(self.Amount * BankAcount.ROI) / 100
        print("Interest Amount :",Interest)

b1=BankAcount()
b2=BankAcount()

b1.Display()
b1.Deposit()
b1.CalculateInterest()
print()

b2.Display()
b2.Withdraw()
b2.CalculateInterest()
print()



    

    