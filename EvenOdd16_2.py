# Write a program which contains one function named as ChkNum() which accepts one parameter as number.If number is even then it should display "Even number" otherwise display "Odd number" on console.

def ChkNum(No):

    if No%2==0:
        print("Even Number :",No)
    else:
        print("Odd Number :",No)
    
def main():
    num=int(input("Enter any number :"))

    Ret=ChkNum(num)


if __name__=="__main__":
    main()