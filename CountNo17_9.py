def CountDigits(num):
    count = 0
    while num > 0:
        count += 1
        num = num // 10 #removes last digit
    return count

num = int(input("Enter a number: "))
print(CountDigits(num))
