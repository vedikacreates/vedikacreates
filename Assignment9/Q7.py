# Armstrong number or not

def count(num):
    if num == 0:
        return 0 
    else:
        return 1 + count(num//10)

def armstrong(num,digits):
    if num == 0:
        return 0
    digit = num % 10
    return digit ** digits + armstrong(num // 10,digits)

num = int(input('Enter number:'))
digits = count(num)
if armstrong(num,digits) == num:
    print(f'{num} is a armstrong number')
else:
    print(f'{num} is not a armstrong number')
