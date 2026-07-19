# count number of digits and letters in a string.

str = input('Enter string: ')

count1 = 0
count2 = 0

for ch in str:
    if ch.isdigit():
        count1 += 1
    elif ch.isalpha():
        count2 += 1
print(f'Number of digits: {count1}\nNumber of letters: {count2}')
