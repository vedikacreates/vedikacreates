# snake ladder pattern

def snakeladder(num):
    ladder = []
    for i in range(10):
        row = []
        for j in range(10):
            row.append(num)
            num += 1
        if i % 2 == 1:
            row.reverse()
        ladder.append(row)
    return ladder
num = 1
res = snakeladder(num)
for row in res:
    print(row)