# write a lambda function using filter() which accepts a list of string and returns a list of string having length greater than 5.

def main():
    List=list(input("Enter any string:").split())
    print(List)

    Fdata=list(filter(lambda str:len(str)>5,List)) # or lambda str : sum(1 for i in str)>5
    print("list of str greater than 5 is :",Fdata)

if __name__=="__main__":
    main()