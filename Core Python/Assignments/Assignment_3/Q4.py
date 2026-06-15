#Write a program to input all sides of a triangle and check whether triangle is valid or not.

#Take input
s1=float(input('Enter side1:'))
s2=float(input('Enter side2:'))
s3=float(input('Enter side3:'))
#apply condition 
if (s1+s2)>s3 and (s2+s3)>s1 and (s1+s3)>s2:
    print('Triangle is valid')
else:
    print('Triangle is invalid')
