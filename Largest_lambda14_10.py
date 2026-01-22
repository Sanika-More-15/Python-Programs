# write a lambda function which accepts three numbers and return largest number.

Largest=lambda No1,No2,No3 :No1 if (No1>=No2) else (No2 if No2>=No3 else No3)
        #if No1 >= No2 and No1 >= No3:
        #   return No1
        #else:
        #    if No2 >= No3:
        #        return No2
        #    else:
         #       return No3


def main():
    No1=int(input("Enter 1st number :"))
    No2=int(input("Enter 2nd number :"))
    No3=int(input("Enter 3rd number :"))

    Ret=Largest(No1,No2,No3)
    print(Ret,"is the largest number")

if __name__=="__main__":
    main()