#number is not divisible by 2 and 3

n = int(input('Enter n:'))
for i in range(1,n+1):
    n2 = i % 2
    n3 = i % 3
    if(n2 != 0 and n3 != 0):
        print(i)