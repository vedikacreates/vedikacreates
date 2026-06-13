#days, year, and weeks

#take input
days = int(input('Enter the Days:'))

#perform operations
#calculate years
years = days // 365
days = days % 365

#calculate weeks
weeks = days // 7
days = days % 7

#display result
print(f'Year : {years}')
print(f'Weeks : {weeks}')
print(f'Days : {days}')