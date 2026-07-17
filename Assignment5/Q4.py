# Armstrong number in given range

start = int(input("Enter start: "))
end = int(input("Enter end: "))

for num in range(start, end + 1):
    temp = num
    count = 0

    # Count digits
    while (temp > 0):
        count += 1
        temp //= 10

    temp = num
    total = 0

    # Find Armstrong sum
    while (temp > 0):
        digit = temp % 10

        value = 1
        for i in range(count):
            value *= digit

        total += value
        temp //= 10

    if total == num:
        print(num, end=' ')