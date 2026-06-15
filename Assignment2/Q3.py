#feet and inches into meter and centimeter

#take input
feet = int(input('Enter the feet:'))
inches = int(input('Enter the inches:'))

#perform operations
m = feet * 0.3048
cm = inches * 2.54

#disply
print(f'The feet in meter is {m}m.')
print(f'The inches in centimeters is {cm}cm.')
