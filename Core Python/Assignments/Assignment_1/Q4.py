#Write a program to enter P, T, R and calculate simple Interest.

#take input
p=float(input('Enter principle amount:'))
r=float(input('Enter rate:'))
t=float(input('Enter time:'))

#perform operation 
si=p*t*r/100

#Display result
print(f'Simple interest of amount {p} with {r} interest and {t} years of time is {si}')