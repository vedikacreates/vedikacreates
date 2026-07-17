# Calculate total amount of ticket

n = int(input('Enter number of passengers:'))
ticketamount = int(input('Enter the amount of ticket:'))
totalticket = 0

for i in range(1,n+1):
    age= int(input(f'Enter age of passenger {i}:'))
  
    if (age < 12):
        ticket = ticketamount - ticketamount/100*30
    
    elif(age > 59):
        ticket = ticketamount - ticketamount/100*50
    else:
        ticket = ticketamount

    totalticket += ticket

print('The total amount of ticket is :',totalticket)

