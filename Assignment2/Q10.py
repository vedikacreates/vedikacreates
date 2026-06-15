#notes needed for representing that amount

#take input
Amount = int(input('Enter the Amount:'))

#perform operation
n500 = Amount // 500
Amount = Amount % 500
n200 = Amount // 200
Amount = Amount % 200
n100 = Amount // 100
Amount = Amount % 100
n50 = Amount // 50
Amount = Amount % 50
n20 = Amount // 20
Amount = Amount % 20
n10 = Amount // 10
Amount = Amount % 10

#disply
print(f'The notes for amount are {n500} of 500, {n200} 0f 200, {n100} of 100, {n50} of 50, {n20} of 20 and {n10} of 10.')
