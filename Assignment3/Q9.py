#WAP to check profit and loss

#take input
cp = int(input('Enter the cost price:'))
sp = int(input('Enter the selling price:'))

#perform operation
amount = sp - cp

#check conditions
if(amount > 0):
    print('profit.')
elif(amount < 0):
    print('loss.')
else:
    print('There is no profit or loss.')


