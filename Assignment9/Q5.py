# sum of digits

def sumOfDigits (num):
    if(num==0):
        return 0
    else:
        return num % 10 + sumOfDigits(num//10 )

num = int(input('Enter the number: '))
res = sumOfDigits(num)
print(f'Sum of digits of a number is {res}.')
