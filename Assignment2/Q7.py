#swaping of two numbers without using third variable

#take input
A = int(input('Enter the value of A:'))
B = int(input('Enter the value of B:'))

#perform operations
A = A + B
B = A - B
A = A - B

#disply result
print(f'The value of A and B after swaping is {A} and {B}.')
