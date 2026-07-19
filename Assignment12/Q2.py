# Remove the nth Index Character from a Non-Empty string

n = int(input('Enter index: '))
str = 'I am good !'

if 0 <= n and n < len(str):
    str = str[:n] + str[n+1:]
    print(f'String after removing index {n}: {str}')
else:
    print('Invalid index')
