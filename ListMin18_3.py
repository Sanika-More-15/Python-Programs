def MinOfList(lst):
    min = lst[0]
    for i in lst:
        if i<min:
            min=i
    return min

numbers = list(map(int,input("Enter numbers :").split()))
print(MinOfList(numbers))
