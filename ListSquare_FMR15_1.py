# write a lambda function using map() which accepts a list of numbers and return a list of squares of each number.

def Square(Num):

    return Num**2

def main():
    
    #L1=[10,20,30,40,50]
    L1=list(map(int,input("enter numbers :").split()))   #.split() → splits string by spaces
    print(L1)                                            # map(int, ...) → converts each string to integer
                                                         # list() → converts result into a list
    MData=list(map(Square,L1))
    print(MData)

if __name__=="__main__":
    main()