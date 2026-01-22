# write a lambda function using filter() which accepts a list of numbers and returns a list of odd numbers.

def main():
    List=list(map(int,input("Enter list of numbers :").split()))
    print(List)

    FData=list(filter(lambda No:No%2==1,List))
    print("List of Odd numbers is :",FData)

if __name__=="__main__":
    main()