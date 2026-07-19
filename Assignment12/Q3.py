# Detect if Two Strings are Anagrams

str1 = input('Enter string: ')
str2 = input('Enter string: ')

if sorted(str1) == sorted(str2):
    str2 = ''
print(str1)
print(str2)
