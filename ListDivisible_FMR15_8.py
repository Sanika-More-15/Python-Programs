# write a lambda function using filter() which accepts a list of numbers and returns the list of numbers divisible by both 3 nad 5.

def main():
    List=list(map(int,input("Enter any string:").split()))
    print(List)

    Fdata=list(filter(lambda num:num%3==0 or num%5==0,List))
    print("List of numbers divisible by both 3 and 5",Fdata) 

if __name__=="__main__":
    main()