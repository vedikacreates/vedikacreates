#WAP to print all numbers in a range divisible by given number

n = int(input('Enter n:'))
num = 0
for i in range(1,25):
    num = i % n
    if(num == 0):
        print(i)
