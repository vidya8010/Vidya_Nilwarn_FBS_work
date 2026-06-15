#Write a Program to input two angles from user and find third angle of the triangle.

#Take input
a1=float(input('Enter angle 1:'))
a2=float(input('Enter angle 2:'))

#Perform operation
a3=180-(a1+a2)

#Display result
print(f'Third angle of triangle is {a3}')