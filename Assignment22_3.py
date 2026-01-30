class Arithmetic:
    Ans=0

    def __init__(self):
        self.Value1=0
        self.Value2=0

    def Accept(self):
        self.Value1=int(input("Enter value 1 :"))
        self.Value2=int(input("Enter value 2 :"))

    def Addition(self):
        Arithmetic.Ans= self.Value1 + self.Value2
        print("Addition :",Arithmetic.Ans)

    def Subtraction(self):
        Arithmetic.Ans= self.Value1 - self.Value2
        print("Suntraction :",Arithmetic.Ans)
    
    def Multiplication(self):
        Arithmetic.Ans= self.Value1 * self.Value2
        print("Multiplication :",Arithmetic.Ans)

    def Division(self):
        
        if self.Value2==0:
            print("Division by Zero Error")
        else:
            Arithmetic.Ans= self.Value1 / self.Value2
            print("Division :",Arithmetic.Ans)
            


obj1=Arithmetic()
obj1.Accept()
obj1.Addition()
obj1.Subtraction()
obj1.Multiplication()
obj1.Division()
