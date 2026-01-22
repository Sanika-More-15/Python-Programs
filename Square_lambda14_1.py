# Write a lambda function which accepts one number and returns square of that number.
# Syntax [ lambda keyword : expression ]

Square=lambda num : (num**2)

def main():

    No=int(input("Enter a any number :"))

    Ret=Square(No)
    print("Square of Number is :",Ret)

if __name__=="__main__":
    main()