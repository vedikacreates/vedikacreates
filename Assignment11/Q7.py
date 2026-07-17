# numbers, squares, cubes

def numbers(li):
    squares = []
    cubes = []
    for i in li:
        squares.append(i**2)
        cubes.append(i**3)
    return squares,cubes

li = [1,2,3,4,5]
squares,cubes = numbers(li)
print(f'numbers: {li}\nsquares: {squares}\ncubes: {cubes}')
