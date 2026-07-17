# sum of series

def factorial(n):
    if (n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)

def sumOfSeries(n):
    if(n==1):
        return 1
    return sumOfSeries(n-1) + factorial(n)

n = int(input('Enter n:'))
res = sumOfSeries(n)
print(f'Sum of factorial of numbers from 1 to {n} is {res}')
