#Write a program to find sum of digits using recursion.
def sumOfDigit(n):
    if n==0:
        return 0
    else:
        d=n%10
        return d+sumOfDigit(n//10)

n=int(input('Enter number:'))
res=sumOfDigit(n)
print(res)