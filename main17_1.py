import Arithmatic17_1

def main():
    no1=int(input("Enter 1st num :"))
    no2=int(input("enter 2nd num :"))

    Ret=Arithmatic17_1.Add(no1,no2)
    Ret=Arithmatic17_1.Sub(no1,no2)
    Ret=Arithmatic17_1.Mult(no1,no2)
    Ret=Arithmatic17_1.Div(no1,no2)

if __name__=="__main__":
    main()
