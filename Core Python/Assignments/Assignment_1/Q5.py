#Write a program to enter P, T, R and calculate Compound Interest.

#take input
p=float(input('Enter principle amount:'))
r=float(input('Enter rate:'))
t=float(input('Enter time:'))

#perform operation 
ci=(p*(1+r/100)**t)-p

#Dipsplay result
print(f'Compound interest of amount {p} with {r} interest and {t} years of time is {ci}')
