#swaping of two nummbers using third variable

#take input
A = int(input('Enter the value of A:'))
B = int(input('Enter the value of B:'))

#perform operation
temp = A
A = B
B = temp

#disply result
print(f'The value of A after swaping is {A} and the value of B after swaping is {B}.')
