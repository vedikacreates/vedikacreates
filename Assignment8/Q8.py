# palidrome or not

def palindrome(n):
    temp = n
    rev = 0
    while(temp > 0):
        digit = temp % 10
        temp = temp // 10
        rev = rev * 10 + digit

    if(n == rev):
        return (f'{n} is a palindrome number')
    else:
        return (f'{n} is not a palindrome number')

n = int(input('Enter number:'))
res = palindrome(n)
print(res)
