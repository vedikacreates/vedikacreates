#calculate total electricity bill

#take input
units = int(input('Enter the electricity units:'))

#check conditions
if(units <= 50):
    bill = units * 0.50
elif(units <= 150):
    bill = (50 * 0.50) + (units - 50)*0.75
elif(units <= 250):
    bill = (50 * 0.50) + (100 * 0.75) + (units - 150) * 1.20
else:
    bill = (50 * 0.50) + (100 * 0.75) + (100 * 1.20) + (units - 250) * 1.50

#perform operations
totalbill = bill + (bill / 100 * 20)

#disply result
print('The total electricity bill is: ',totalbill)
