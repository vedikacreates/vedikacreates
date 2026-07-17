# Area of Circle

def areaOfCircle(r):
    Area = 3.14 * r ** 2
    return Area

redius = int(input('Enter redius of circle: '))
res = areaOfCircle(redius)
print('Area of Circle is ',res)
