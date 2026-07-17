# number is present or not

def isPresent(li,num):
    
    while num in li:
        return True
    else:
        return False

num= int(input('Enter the number: '))
li = [20,40,50,60,70,10]
res = isPresent(li,num)
if res == True:
    print(f'{num} is present in the list.')
else:
    print(f'{num} is not present in the list')
