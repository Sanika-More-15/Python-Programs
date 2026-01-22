# Write a lambda function which accepts two numbers and return addtion.

Add=lambda No1,No2 : No1*No2

def main():
    num1=int(input("Enter First number :"))
    num2=int(input("Enter Second number :"))

    Ret=Add(num1,num2)
    print("Multiplication is :",Ret)

if __name__=="__main__":
    main()