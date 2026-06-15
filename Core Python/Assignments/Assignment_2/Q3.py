#Convert distant given in feet and inches into meter and centimeter.

#Take input
f=float(input('Enter feet:'))
i=float(input('Enter inches:'))

#Perform operation 

#centmeter conversion
cm=(f*12+i)*2.54
#meter conversion
m=cm/100

#Display result
print(f'Conversion of {f} feets and {i} inches into {cm}cm and {m}m.')