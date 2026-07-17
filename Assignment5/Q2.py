# percentage and average percentage

n = int(input('Enter number of students:'))
print()
total_percentage = 0

for i in range(1,n+1):
    total_marks = 0
    print(f'Enter marks of student {i}:')
    print()

    for j in range(1,6):
        marks = int(input(f'Enter marks of subject {j}:'))
        total_marks += marks

    percentage = (total_marks / 500)*100
    print('percentage =',percentage)
    print()
    total_percentage += percentage

average_percentage = total_percentage /n
print('Average percentage of all students =',average_percentage)
