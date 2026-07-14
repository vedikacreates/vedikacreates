#armstrong number

num = int(input('Enter the number:'))
temp = num 
count = 0

while (temp > 0):
    d= temp % 10
    temp = temp // 10
    count += 1
sum = 0
temp = sum
while(temp > 0):
    d = temp % 10
    sum = sum + (d**count)
    temp = temp // 10
if(sum == num):
    print('It is a Armstrong number.')
else:
    print('It is not a Armstrong number.')
