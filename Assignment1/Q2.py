#percentage of student
 
#take input
m = int(input('Enter the marks in Math:'))
e = int(input('Enter the marks in English:'))
s = int(input('Enter the marks in Science:'))
h = int(input('Enter the marks in History:'))
g = int(input('Enter the marks in Geography:'))
totalmarks = int(input('Enter the Total Marks:'))

# perform operations
sum = m + e + s + h + g
percentage = sum / totalmarks * 100

#disply result
print(f'The percentage of the student is {percentage}%.')
