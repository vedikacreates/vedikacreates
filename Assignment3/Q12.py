#find the number is palindrome or not

#take input
num = int(input('Enter the three digit number:'))

#perform operations
first = num // 100
last = num % 10 

#check conditions
if(first == last):
    print('The number is a palindrome.')
else:
    print('The number is not palindrome.')
    