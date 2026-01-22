# Write a lambda function which accepts one number and returns True if dibisible by 5

Divisible=lambda num : (num%5==0)

def main():

    No=int(input("Enter a number :"))

    Ret=Divisible(No)

    if Ret==True:
        print(No,"is divisible by 5")

if __name__=="__main__":
    main()