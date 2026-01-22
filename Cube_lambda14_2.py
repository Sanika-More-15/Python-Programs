# Write a lambda function which accepts one number and returns cube of that number.

Cube=lambda num : (num**3)

def main():
    No=int(input("Enter a number :"))

    Ret=Cube(No)
    print("Cube of number is :",Ret)

if __name__=="__main__":
    main()