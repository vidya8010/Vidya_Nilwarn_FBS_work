#Write a program to swap two numbers using third variable.
n1=int(input('Enter num1:'))
n2=int(input('Enter num2:'))

#Perform operation
n3=n1
n1=n2
n2=n3

#Display result
print(f'After Swapping n1:{n1} and n2:{n2}')