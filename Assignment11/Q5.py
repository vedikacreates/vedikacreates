# intersection elements

def intersection(li1,li2):
    intern=[]
    for i in li1:
        if i in li2:
            intern.append(i)
    return intern
li1 = [1,2,3,4,5]
li2 = [5,4,3,6,7]
res = intersection(li1,li2)
print('Intersection of li1 and li2:',res)