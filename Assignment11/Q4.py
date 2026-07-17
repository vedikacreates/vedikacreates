# union of two lists

def union(li1,li2):
    unique = list(set(li1 + li2))
    return unique
li1 = [1,3,5,7]
li2 = [2,4,6,9,7,4,1]
res=union(li1,li2)
print('Unions of li1 and li2 are:',res)
