#Write a program to check if given 3 digit number is a palindrome or not.

num=int(input('Enter three digit number:'))
n=num

d1=n%10
n=n//10

d2=n%10
n=n//10

d3=n%10
n=n//10

rev_num=d1*100+d2*10+d3

if num==rev_num:
    print(f'{num} is palindrome')
else:
    print(f'{num} is not palindrome')