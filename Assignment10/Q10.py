# divisible by m and n

def divisible(li,m,n):
    li1 = []
    for i in li:
        if i % m == 0 and i % n ==0:
            li1 += [i]
    return li1

m = int(input('Enter m:'))
n = int(input('Enter n:'))
li = [10,20,30,40,50,60,70,80]
res = divisible(li,m,n)
print(f'Numbers which are divisible by {m} and {n} in the list are: {res}')
