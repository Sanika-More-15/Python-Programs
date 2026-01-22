# write a lambda function using filter() which accepts a list of numbers and returns the list of numbers divisible by both 3 nad 5.
from functools import reduce
def main():
    List=list(map(int,input("Enter any string:").split()))
    print(List)

    Rdata=reduce(lambda a,b:a*b,List)
    print("product of all elements :",Rdata) 

if __name__=="__main__":
    main()