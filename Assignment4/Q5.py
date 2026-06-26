# check prime number or not

no = int(input('Enter the no:'))
if no<=1:
    print('No is not prime and nor composite.')
else:
    for i in range(2,no):
        if no % i == 0:
            flag = 1
            break
    if(flag == 0):
        print('It is a prime number.')
    else:
        print('Not a prime number.')
