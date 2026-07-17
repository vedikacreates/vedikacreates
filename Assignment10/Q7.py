# remove occurence of the element

def occurence(li,num):
    li1 = []
    for i in li:
        if num != i:
            li1 = li1 + [i]
    return li1

num = int(input('Enter number that you want to remove:'))
li = [10,20,30,10,40,10,50,60,60,30,70,90]
res = occurence(li,num)
print(f'List after removing {num}: {res}')
