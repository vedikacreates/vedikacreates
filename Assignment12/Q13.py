# count the occurrences of each word in a string

string = input('Enter string: ')

str = string.split()
for i in range(len(str)):
    if i == str.index(str[i]):
        print(str[i], ':', str.count(str[i]),end =' ')
