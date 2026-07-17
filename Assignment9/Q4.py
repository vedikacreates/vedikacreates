# reverse a number

def reverse (num,rev):
    if (num == 0):
        return rev
    else:
        return reverse(num//10,rev * 10 + num %10)

num = int(input('Enter the number:'))
res=reverse(num,0)
print('Reversed number:',res)
