#Write a program to find factorial using recursion.
def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)

n=int(input('Enter number:'))
res=fact(n)
print(res)