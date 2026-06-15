#Find the sum of three-digit number.

#take input
num=int(input('Enter three digit number:'))

#Perform operations
d1=num%10
num=num//10

d2=num%10
num=num//10

d3=num%10
num=num//10

sum=d1+d2+d3

#Display result
print(f'Sum of three digit is {sum}')