# num is +ve -ve or zero

def ChkNum(num):
    
    if num==0:
        print("It is zero")
    elif num>0:
        print("Positive number")
    else:
        print("Negative number")


def main():

    num=int(input("Enter any number :"))
    Ret=ChkNum(num)

if __name__=="__main__":
    main()