# sum of n numbers

def sumOfn (n):
    if (n==0):
        return 0
    else:
        return n + sumOfn(n-1)

n = int(input('Enter n:'))
res = sumOfn(n)
print(f'Sum of numbers from 1 to {n} is {res}')
