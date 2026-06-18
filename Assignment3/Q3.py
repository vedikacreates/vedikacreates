#WAP to check triangle is valid or not 

#take input
angle1 = int(input('Enter first angle:'))
angle2 = int(input('Enter second angle:'))
angle3 = int(input('Enter third angle:'))

#perform operation
sum = angle1 + angle2 + angle3

# check conditions
if(sum == 180):
    print('The triangle is valid.')
else:
    print('The triangle is invalid.')
    