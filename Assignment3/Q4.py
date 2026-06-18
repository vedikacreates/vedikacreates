#check traingle is valid or not by cheking sides

#take input
a = int(input('Enter the first side of the triangle:'))
b = int(input('Enter the second side of the triangle:'))
c = int(input('Enter the third side of the triangle:'))

#check conditions
if((a+b>c) and (b+c>a) and (a+c>b)):
    print('The triangle is valid.')
else:
    print('The triangle is invalid')
    