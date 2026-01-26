# addition of 2 numbers.

def Add(No1,No2):

    Ans=0
    Ans=No1+No2
    print("Addition is :",Ans)

def main():

    no1=int(input("Enter 1st Number :"))
    no2=int(input("Enter 2nd number :"))

    Ret=Add(no1,no2)

if __name__=="__main__":
    main()