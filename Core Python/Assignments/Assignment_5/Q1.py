#Write a program to prompt user to enter userid and password. If Id and
#password is incorrect give him chance to re-enter the credentials. Let him try 3
#times. After that program to terminate.
userid='vidya123'
password='123'
n=2
user_id=input('Enter userid:')
user_pass=input('Enter password:')
if user_id==userid and user_pass==password:
     print('logged in successfully') 
else:
     while n>=1:
          user_id=input('enter userid:')
          user_pass=input('enter password:')
          n-=1
     else:
         print('You failed three attemts also ')