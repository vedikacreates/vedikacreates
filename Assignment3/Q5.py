# check the type of triangle

#take input
a = int(input('Enter one side of triangle:'))
b = int(input('Enter second side of triangle:'))
c = int(input('Enter third side of triangle:'))

#check conditions
if(a == b == c):
    print('It is a Equilateral triangle.')
elif(a == b or b == c or a == c):
    print('It is Isolated triangle.')
elif(a != b or b != c or a != c):
    print('It is Scalene triangle.')
else:
    print('The triangle is invalid.')
    