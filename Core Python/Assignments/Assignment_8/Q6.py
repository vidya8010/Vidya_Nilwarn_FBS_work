#Write a program to find print the following Fibonacci series using
#functions:
#1 1 2 3 5 8 n terms
def fibo(n):
    a=-1
    b=1
    for i in range(1,n+1):
        c=a+b
        print(c)
        a=b
        b=c
n=int(input('Enter n:'))
fibo(n)