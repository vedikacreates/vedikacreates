# maximum and minimum element in the list

def maxMin(li):
    size = len(li)
    max = li[0]
    min = li[0]
    for i in range(1,size):
        if max < li[i]:
            max = li[i]
      
    for i in range(1,size):
        if min > li[i]:
            min = li[i]
            
    return max,min

li = [100,40,50,30,20]
maximum,minimum = maxMin(li)
print('Maximum element in the list is:', maximum)
print('Minimum element in the list is:', minimum)