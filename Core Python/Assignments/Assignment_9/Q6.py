#Write a program to print Fibonacci series using recursion.
def fibo(n):
    if n<=1:
        return n
    else:
        return fibo(n-1)+fibo(n-2)
n=10
for i in range(0,n):
    print(fibo(i))