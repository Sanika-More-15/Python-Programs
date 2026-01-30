class Numbers:

    def __init__(self):
        self.Value=int(input("Enter a Number :"))
        
    def CheckPrime(self):
        if self.Value<=1:
            print("Not a Prime Number")
            return
        
        for i in range(2,self.Value):
            if self.Value%i==0:
                print("Not a prime number")
                return

        print("Prime Number")
        
    def CheckPerfect(self):
        sum=0
        for i in range(1,self.Value):
            if self.Value%i==0:
                sum=sum+i

        if sum==self.Value:
            print("Perfect number")
        else:
            print("Not a Perfect number")
        
    def Factors(self):
        for i in range(1,self.Value+1):
            if self.Value%i==0:
                print(i)
            
    def SumFactors(self):
        total=0
        for i in range(1,self.Value+1):
            if self.Value%i==0:
                total=total+1
        print("sum of factors :",total)
        

b1=Numbers()
b1.CheckPrime()
b1.CheckPerfect()
b1.Factors()
b1.SumFactors()



    

    