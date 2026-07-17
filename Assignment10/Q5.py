# sum of all elements in the list

def sumofList(li):
    sum = 0
    for i in range(len(li)):
        sum = sum + li[i]
    return sum

li = [10,20,30,40,50]
res = sumofList(li)
print('Sum of all elements in the list is:',res)
