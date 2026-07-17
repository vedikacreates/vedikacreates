# remove duplicates

def removeDuplicates(li):
    li1 = []
    
    for i in li:
        if i not in li1:
            li1 = li1 + [i]
    return li1

li = [10,20,10,20,30,40,30,50,60,60]
res = removeDuplicates(li)
print('List after removing duplicates:',res)