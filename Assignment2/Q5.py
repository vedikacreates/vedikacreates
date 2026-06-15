#Total salary of employee

#take input
basic = int(input('Enter the Value of basic salary:'))

#operations
DA = basic * 10/100
TA = basic * 12/100
HRA = basic * 15/100
totalSalary = basic + DA + TA + HRA

#disply
print(f'The total salary of employee is {totalSalary}rs.')
