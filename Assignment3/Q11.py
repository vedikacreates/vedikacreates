#calculate total amount of ticket to travel for the five people.

#take input
ticket = int(input('Enter the ticket amount:'))

#check conditions
age1 = int(input('Enter the age of first person:'))
if(age1 < 12):
    amount1 = ticket - ticket/100*30
elif(age1 > 59):
    amount1 = ticket - ticket/100*50
else:
    amount1 = ticket

age2 = int(input('Enter the age of second person:'))
if(age2 < 12):
    amount2 = ticket - ticket/100*30
elif(age2 > 59):
    amount2 = ticket - ticket/100*50
else:
    amount2 = ticket

age3 = int(input('Enter the age of third person:'))
if(age3 < 12):
    amount3 = ticket - ticket/100*30
elif(age3 > 59):
    amount3 = ticket - ticket/100*50
else:
    amount3 = ticket

age4 = int(input('Enter the age of fourth person:'))
if(age4 < 12):
    amount4 = ticket - ticket/100*30
elif(age4 > 59):
    amount4 = ticket - ticket/100*50
else:
    amount4 = ticket

age5 = int(input('Enter the age of fifth person:'))
if(age5 < 12):
    amount5 = ticket - ticket/100*30
elif(age5 > 59):
    amount5 = ticket - ticket/100*50
else:
    amount5 = ticket

#perform operation
totalamount = amount1 + amount2 + amount3 + amount4 + amount5

#disply result
print(f'The total amount of ticket required is {totalamount}.')

