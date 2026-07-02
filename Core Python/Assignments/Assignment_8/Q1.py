#1. Write a program to calculate area of rectangle
def areaRectangle(l,b):
    return l*b
l=float(input('Enter length:'))
b=float(input('Enter breadth:'))
area=areaRectangle(l,b)
print(f'Area of rectangle is {area}')
