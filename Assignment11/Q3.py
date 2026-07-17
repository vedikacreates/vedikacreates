# sort element according to length of element

def sortElement(li):
    li.sort(key=len)
li = ['banana','kivi','apple','pineapple','grapes']
sortElement(li)
print('Sorted list:',li)