#roots of equation

#take input
a = int(input('Enter the value of a:'))
b = int(input('Enter the value of b:'))
c = int(input('Enter the value of c:'))

#operation operations
d = b**2 - 4*a*c
r1 = (-b + d*0.5) / (2*a)
r2 = (-b - d*0.5) / (2*a)

#disply result
print(f'The roots of equation are {r1} and {r2}.')
