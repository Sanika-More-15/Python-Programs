def SumOfList(lst):
    total = 0
    for i in lst:
        total = total + i
    return total

numbers = list(map(int,input("Enter numbers :").split()))
print(SumOfList(numbers))
