# sum of prime number upto n

def isPrime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def sumPrime(n):
    sum = 0
    for i in range(2, n + 1):
        if isPrime(i):
            sum += i
    return sum

n = int(input("Enter n: "))
print(f'Sum of prime numbers from 1 to {n} is {sumPrime(n)}')
