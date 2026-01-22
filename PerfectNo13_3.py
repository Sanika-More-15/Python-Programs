# Write a program which accepts one number and checks whether it is perfect no or not.

def PerfectNo(num):
    sum=0
    for i in range(1,num):
        if num%i==0:
            sum=sum+i

    if sum==num:
        print("Perfect number")
    else:
        print("Not a Perfect number")

def main():

    num=int(input("Enter any number :"))

    Ret=PerfectNo(num)

if __name__=="__main__":
    main()