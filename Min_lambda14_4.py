# Write a lambda function which accepts two numbers and returns maximun number.

Max=lambda No1,No2 : (No1<No2 or No2<No1)

def main():

    No1=int(input("Enter 1st number :"))
    No2=int(input("Enter 2nd number :"))

    if No1<No2:
        print(No1," is  Minimum number")
    else:
        print(No2," is Minimum number")

    Ret=Max(No1,No2)

if __name__=="__main__":
    main()