# cubes of elements in the list

def cubes(li):
    cube = []
    for i in li:
        cube = cube + [i**3]
    return cube

li = [ 1,2,3,4,5]
res = cubes(li)
print('Cubes:',res)