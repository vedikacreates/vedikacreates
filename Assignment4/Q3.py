#sum of series upto n

#using for loop
n = int(input('Enter n:'))
sum = 0
for i in range(1,n+1,1):
    sum = sum + i
print(sum)

#using while loop
n = int(input('Enter the n:'))
i = 1
sum = 0
while(i<=n):
    sum = sum + i
    i = i+1
print(sum)
