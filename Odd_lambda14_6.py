# Write a lambda function which accepts one number and returns True if number is odd otherwise False.

Even=lambda num : (num%2==1)

def main():
    No=int(input("Enter any number :"))

    Ret=Even(No)

    if Ret==True:
        print(No,"is Odd")
    else:
        return False
    
if __name__=="__main__":
    main()