# check number is prime or not

def checkPrime (d,num):
    if d == num:
        return True
    if num % d == 0: 
        return False
    return checkPrime(d+1,num)

num = int(input('Enter number:'))
if num < 2:
    print(f'{num} is not a prime number.')
elif checkPrime(2,num):
    print(f'{num} is a prime number.')
else:
    print(f'{num} is not a prime number.')
    