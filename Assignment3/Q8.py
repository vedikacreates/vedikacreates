#check whether a girl or boy is eligible for marriage or not

#take input
gender = input('Enter the gender:')
age = int(input('Enter the age:'))

#check conditions
if(gender == 'female'):
    if(age > 18):
        print('The girl is eligible for marriage.')
    else:
        print('The girl is not eligible for marriage.')
else:
    if(age > 21):
        print(' The boy is eligible for marriage.')
    else:
        print('The boy is not eligible for marriage.')

