#Write a program to prompt user to enter userid and password. After verifying
#userid and password display a 4 digit random number and ask user to enter the
#same. If user enters the same number then show him success message otherwise
#failed. (Something like captcha)

#check Username and password on the basisi of captcha to logged in successfull and invalid credentials
import random

#Fixed username and password
al_u_name='vidya'
al_pass='v123'

#Take user input
u_name=input('Enter username:')
u_pass=input('Enter password:')

#Check condition are matched or not
if u_name==al_u_name and u_pass==al_pass:
    #Generate captcha
    captcha=random.randint(1000,9999)
    #Show captcha to user
    print('Your captcha:',captcha)
    #Input captcha from user
    u_captcha=int(input('Enter above captcha:'))
    #Check captcha
    if u_captcha==captcha:
        print('Logged in successfull')
    else:
        print('Invalid captcha')
else:
    print('Invalid credentials')