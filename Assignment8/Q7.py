# reverse number

def reverse_number(num):
    reverse = 0
    while num > 0:
        digit = num % 10
        num = num // 10
        reverse = reverse * 10 + digit
    return reverse

n = int(input("Enter a number: "))
print("Reversed number:", reverse_number(n))
