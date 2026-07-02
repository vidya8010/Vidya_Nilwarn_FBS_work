#Write a program to find sum of following series using functions :
#a. 1+ 2 + 3 + 4+..... + n
#b. 1!+ 2! + 3! + 4!+..... + n!
#c. 1^1 + 2^2 + 3^3+ ...... n^n

def sumSeries(n):
    sum=0
    for i in range(1,n):
        sum+=i
    print(f'Summation upto {n} numbers is {sum}')
def sumFactorial(n):
    temp=n
    sum=0
    while n>0:
        fact=1
        for i in range(1,n+1):
            fact=fact*i
        sum+=fact
        n-=1
    print(f'Summation of factoraila upto {temp} numbers is {sum}')
def sumPower(n):
    temp=n
    total=0
    while(n>0):
        power=1
        for i in range(1,n+1):
            power=i**i
        total=total+power
        n-=1
    print(f'Summation of power upto {temp} numbers is {total}')

n=int(input('Enter n:'))
sumSeries(n)
sumFactorial(n)
sumPower(n)