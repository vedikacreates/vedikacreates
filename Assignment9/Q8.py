# m to the power n

def power(m,n):
    if n == 0:
        return 1
    return m * power(m,n-1)

m = int(input('Enter the m: '))
n = int(input('Enter the n: '))
res = power(m,n)
print(f'{m} to the power {n} is {res}.')
