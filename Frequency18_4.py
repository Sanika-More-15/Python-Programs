def Frequency(lst, num):
    count = 0
    for i in lst:
        if i == num:
            count += 1
    return count


def main():
    n = int(input("Enter number of elements: "))
    lst = []

    for i in range(n):
        value = int(input("Enter element: "))
        lst.append(value)

    num = int(input("Enter number to find frequency: "))

    result = Frequency(lst, num)
    print("Frequency of", num, "is:", result)


if __name__ == "__main__":
    main()

