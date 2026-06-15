#reverce the three digit number

#take input
num = int(input('Enter three digit number:'))

#perform operations
hundred = num // 100
tens = num // 10 % 10
ones = num % 10
reverse = ones*100 + tens*10 + hundred

#disply result
print(f'The reversed number is {reverse}.')