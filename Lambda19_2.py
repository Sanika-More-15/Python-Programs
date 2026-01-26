
Power=lambda No1,No2 : No1 * No2

def Main():
    no1=int(input("Enter 1st number :"))
    no2=int(input("Enter 2nd number :"))
    Ret = Power(no1,no2)
    print(Ret)

if __name__=="__main__":
    Main()