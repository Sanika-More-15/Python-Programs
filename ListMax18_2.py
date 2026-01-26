def MaxOfList(lst):
    max = lst[0]
    for i in lst:
        if i>max:
            max=i
    return max

numbers = list(map(int,input("Enter numbers :").split()))
print(MaxOfList(numbers))
