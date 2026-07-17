# check Armstrong number or not

def power(num, p):
    result = 1
    for i in range(p):
        result = result * num
    return result

def armstrong(n):
    temp = n
    count = 0

    while temp > 0:
        count = count + 1
        temp = temp // 10

    temp = n
    sum = 0

    while temp > 0:
        digit = temp % 10
        sum = sum + power(digit, count)
        temp = temp // 10
           

    if(sum == n):
        return (f'{n} is a Armstrong number.')
    else:
        return (f'{n} is not a Armstrong number.')

n = int(input('Enter n:'))
res = armstrong(n)
print(res)
