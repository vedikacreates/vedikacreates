# pattern 3

for i in range(1, 5):
    for j in range(1, 5 - i):
        print(" ", end=" ")
    for j in range(1, i + 1):
        if i == 1:
            print(1, end=" ")
        elif i == 2:
            print(1, end="  ")
        elif i == 3:
            if j == 2:
                print(2, end="  ")
            else:
                print(1, end="  ")
        elif i == 4:
            if j == 2 or j == 3:
                print(3, end="  ")
            else:
                print(1, end="  ")
    print()