# even and odd in seperae list

def evenOdd(li):
    even = []
    odd = []
    for i in li:
        if i % 2 == 0:
            even = even + [i]
        else:
            odd = odd + [i]      
    return even,odd        

li = [1,2,3,4,5,6,7,8,9,10]
even,odd = evenOdd(li)
print('Even numbers are:',even)
print('Odd numbers are:',odd)