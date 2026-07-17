# first n prime numbers

n = int(input('Enter n:'))

prime = 0
i = 2

while prime < n:
    count = 0
    for j in range(1,i+1):
        if(i % j == 0):
            count += 1
    if(count == 2):
        print(i,end = ' ')
        prime += 1
    i += 1