# second largest

def secondLargest(li):
    li.sort()
    return li[-2]
li = [10, 25, 15, 30, 20]
print("Second Largest:",(secondLargest(li)))