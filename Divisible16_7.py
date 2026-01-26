#Divisible by 5

def Divisible(no):

    if no%5==0:
        print("The number is divisible by 5")
    else:
        print("Not divisible")


def main():

    no=int(input("Enter any number :"))

    Ret=Divisible(no)

if __name__=="__main__":
    main()