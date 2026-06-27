#WAP to print all even numbers until n.
n=int(input('Enter n:'))
for i in range(1,n):
    if(i%2==0):
        print(i)