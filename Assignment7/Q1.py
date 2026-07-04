# pattern 1

for i in range(1,6):
    for j in range(1,6):
        if( i + j == 6):
            print('*',end = '')
        else:
            print(' ',end = '')
    for j in range(2,6):
        if(i == j):
            print('*',end = '')
        else:
            print(' ',end = '')
    print()

for i in range(1,6):
    for j in range(1,6):
        if(j == i):
            print('*',end = '')
        else:
            print(' ',end = '')
    for j in range(2,6):
        if( i + j == 6):
            print('*',end = '')
        else:
            print(' ',end = '')
    print()
