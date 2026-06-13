#Compound Interest

#take input
P = int(input('Enter the Principle Amount:'))
R = int(input('Enter the Rate:'))
T = int(input('Enter the Time:'))

#perform operation
CI = P*(1+R/100)**T-P

#display result
print(f'The Compound Interest is {CI}.')
