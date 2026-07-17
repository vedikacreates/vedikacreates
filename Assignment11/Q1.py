# even and odd in two different lists

def evenOdd(li):
    even = []
    odd = []
    for i in li:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    return even,odd
         
li = [1,2,3,4,5,6,7,8,9,10]
even,odd = evenOdd(li)
print('Even:',even)
print('Odd:',odd)