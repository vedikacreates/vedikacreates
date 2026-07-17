#userid and password

UserId = 'abcd'
PassWord = '12345'

attempt = 1

while(attempt <= 3):

    userid = input('Enter userid:')
    password = input('Enter password:')

    if(userid == UserId and password == PassWord):
        print('Login successful')
        break

    else:
        print('Invalid userid and password,try again')
        attempt = attempt + 1
        
else:
    print('Maximum attempts exceeded.')
