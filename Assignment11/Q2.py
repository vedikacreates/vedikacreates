# add two lists and sort it

def sortTwo(li,li1):
    li.extend(li1)
    li.sort()
    return li
li = [1,5,8,3,0]
li1 =[2,6,7,4,9]
sortTwo(li,li1)
print('Sorted list:',li)
