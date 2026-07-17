# sum of all odd numbers between 1 to n

def oddSum(n):
    sum = 0
    for i in range(1,n+1,2):
        sum = sum + i
    return sum

n = int(input('Enter n:'))
res = oddSum(n)
print(f'Sum of odd numbers between 1 to {n} is :',res)
