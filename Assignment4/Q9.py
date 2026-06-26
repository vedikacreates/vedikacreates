#numbers are divisible by 7 and multiple of 5
start= int(input('Enter start:'))
end=int(input('Enter end:'))
for i in range(start,end):
    
    if(i%7==0 and i%5==0):
        print(i)
   