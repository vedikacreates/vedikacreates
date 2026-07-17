# second largest element of the list

def secondLargest(li):
    for i in range(len(li)):
        for j in range(len(li)-1):
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]

li = [10, 25, 15, 30, 20]
secondLargest(li)
print("Second Largest:", li[-2])
