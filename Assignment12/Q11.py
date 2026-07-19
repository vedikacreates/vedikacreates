# count number of lowercase characters in a string

str = input('Enter string: ')

count = 0
for ch in str:
    if ch.islower():
        count +=1
print(count)
