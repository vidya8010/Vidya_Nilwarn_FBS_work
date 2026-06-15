#Write a program to check whether the triangle is equilateral, isosceles or scalene triangle.

s1=float(input('Enter side1:'))
s2=float(input('Enter side2:'))
s3=float(input('Enter side3:'))

if s1==s2==s3:
    print(f'Triangle is equilateral')
elif s1!=s2!=s3:
    print(f'Traingle is scelence')
else:
    print(f'Triangle is isoscales')