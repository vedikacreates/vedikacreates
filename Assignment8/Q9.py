# leap or not

def isLeapYear(year):
    if(year % 4 == 0):
        return (f'{year} is a leap year.')
    else:
        return (f'{year} is not a leap year.')

year = int(input('Enter the year:'))
res = isLeapYear(year)
print(res)
