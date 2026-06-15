#WAP to calculate area of triangle and rectangle

#Take input 
l=float(input('Enter length:'))
b=float(input('Enter base:'))
h=float(input('Enter height:'))

#perform operation 

#Area of reactangle
area_r=l*b

#Area of triangle
area_t=1/2*b*h

#Display result
print(f'Area of triangle is {area_t} and area of rectangle is {area_r}')