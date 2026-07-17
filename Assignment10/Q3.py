# reverse the list

def reverse(li,start,end):
    
    while start < end:
        li[start],li[end] = li[end],li[start]
        start += 1
        end -= 1
    return li

li = [ 10,40,20,50,30]
start = 0
end = len(li)-1
res = reverse(li,start,end)
print('Reversed list:',res)
