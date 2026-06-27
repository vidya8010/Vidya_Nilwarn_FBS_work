#WAP to print Fibonacci series upto n.
a=-1
b=1
n=int(input('Enter number upto print fiboncci series:'))
for i in range(n):
    c=a+b
    print(c)
    a=b
    b=c