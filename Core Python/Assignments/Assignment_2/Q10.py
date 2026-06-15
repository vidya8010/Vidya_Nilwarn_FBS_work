# #10. Write a program to reverse three-digit number.

# Take input

num=int(input('Enter num:'))

#Perform operation 
d1=num%10
num=num//10

d2=num%10
num=num//10

d3=num%10
num=num//10

rev=d1*100+d2*10+d3*1

#Display result
print('Reverse number:',rev)
