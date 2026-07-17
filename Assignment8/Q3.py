# calculation of series

# a.sum of series

def sumOfSeries(num):
    sum = 0
    for i in range(1,n+1):
        sum += i
    return sum

n = int(input('Enter the n:'))
res = sumOfSeries(n)
print(f'Sum of numbers from 1 to {n} is {res}')


# b. sum factorial of series

def factorialOfSeries(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact * i
    return fact

n = int(input('Enter n:'))
res = factorialOfSeries(n)
print(f'Sum of factorial of numbers from 1 to {n} is {res}')


# c. sum of self power series

def powerSeries(n):
    sum = 0
    for i in range(1, n+1):
        sum += i**i
    return sum
n = int(input('Enter n:'))
res = powerSeries(n)
print(f'Sum of power of numbers from 1 to {n} is {res}')