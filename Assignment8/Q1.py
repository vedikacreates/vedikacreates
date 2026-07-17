# Area of rectangle

def areaOfRectangle(l,b):
    Area = l * b
    return Area

a = int(input('Enter length of the rectangle: '))
b = int(input('Enter bridth of the rectangle: '))

res=areaOfRectangle(a,b)
print(f'The area of rectangle is {res} square units.')