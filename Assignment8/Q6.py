# sum of digits

def sumDigits(num):
    temp = num
    sum = 0
    for i in range(1,temp+1):
        digit = temp % 10
        sum = sum + digit
        temp = temp // 10
    return sum
n = int(input('Enter the n:'))
res = sumDigits(n)
print(f'Sum of digits of number is',res)
   