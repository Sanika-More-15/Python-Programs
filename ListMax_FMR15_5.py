# write a lambda function using reduce() which accepts a list of numbers and returns the maximum element.
from functools import reduce

def main():
    List=list(map(int,input("Enter list of numbers :").split()))
    print(List)

    RData=reduce(lambda No1,No2:No1 if (No1>No2) else No2,List)
    print("Maximum number is :",RData)

if __name__=="__main__":
    main()