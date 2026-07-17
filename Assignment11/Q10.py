# sort according to 2nd element of list 

def secondElement(li):
    return li[1]
li = [[1,5],[3,6],[8,2]]
li.sort(key=secondElement)
print('Sorted list:',li)
