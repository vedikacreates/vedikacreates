#Verify the username, password and captcha
username = 'abcd'
passw = '0000'

#take input
userid = input('Enter the userid:')
password = input('Enter the password:')

#check conditions
if(userid == username and password == passw):
    captcha = 1234
    print(captcha)
    Captcha = int(input('Enter the captcha:'))
    if(Captcha == captcha):
        print('login successful.')
    else:
        print('login failed.')
else:
    print('username and password is invalid.')
    

