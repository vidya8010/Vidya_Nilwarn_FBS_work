#Write a program to swap two numbers without using third variable.

#Take input

n1=int(input('Enter num1:'))
n2=int(input('Enter num2:'))



#perform operation 

#method1
n1=n1+n2
n2=n1-n2
n1=n1-n2

#Method2
n1,n2=n2,n1

#Display result
print(f'After Swapping n1:{n1} and n2:{n2}')