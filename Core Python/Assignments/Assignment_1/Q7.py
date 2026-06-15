#Program to Find the Roots of a Quadratic Equation

#take input
a=int(input('Enter a:'))
b=int(input('Enter b:'))
c=int(input('Enter c:'))

#Perform operation
x1=(-b+(b**2-4*a*c)**0.5)/(2*a)
x2=(-b-(b**2-4*a*c)**0.5)/(2*a)

#Display result
print(f'Firts root of quadratic equation is {x1} & second root of quadratic equation is {x2}')

