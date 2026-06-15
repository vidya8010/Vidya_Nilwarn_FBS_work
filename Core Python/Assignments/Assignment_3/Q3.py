#Write a program to input angles of a triangle and check whether triangle is valid or not.
a=int(input('Enter angle 1:'))
b=int(input('Enter angle 2:'))
c=int(input('Enter angle 3:'))

#perform operation 
if a+b+c==180:
    print('Triangle is valid')
else:
    print('Triangle is not valid')