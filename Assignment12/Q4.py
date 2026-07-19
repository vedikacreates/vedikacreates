# New String where the First Character and the Last Character have been Exchanged

str = input('Enter string: ')
str = str[-1] + str[1:-1] + str[0] 
print('Exchanged string:',str)
