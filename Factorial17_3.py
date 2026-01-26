def factorial():
    Num=int(input("Enter Any Number : "))
    fact=1
    for i in range(1,Num+1):
        fact=fact*i
    print("factorial of no is : ",fact)

factorial()