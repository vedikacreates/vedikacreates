#sum of three digit number

#take input
num = int(input('Enter the three digit number:'))

#perform operations
d1 = num % 10
num = num // 10
d2 = num % 10
num = num // 10
d3 = num % 10
num = num // 10
sum = d1 + d2 + d3

#disply result
print(f'Addition of three digit number is {sum}.')
