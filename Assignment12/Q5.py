# to Count the Number of Vowels in a String

str = input('Enter string: ')
count = 0
for i in str:
    if i in 'aeiouAEIOU':
        count += 1
print('Numbers of vowels are:',count)