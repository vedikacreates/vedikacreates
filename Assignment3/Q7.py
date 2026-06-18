#WAP to disply grades of student

#take input
m = int(input('Enter the marks in Math:'))
e = int(input('Enter the marks in English:'))
h = int(input('Enter the marks in History:'))
g = int(input('Enter the marks in Geography:'))
s = int(input('Enter the marks in Science:'))
totalmarks = int(input('Enter total marks:'))

#perform operations
sum = m + e + h + g + s
percentage = sum / totalmarks * 100

#check conditions
if(percentage >= 90):
    print('The student passed with First Class.')
elif(percentage >= 75):
    print('The student passed with Second Class.')
elif(percentage >= 60):
    print('The student passed with Third Class.')
elif(percentage >= 35):
    print('The student passed with Fourth Class.')
else:
    print('The student failed.')


