#Write a program to check if given number is Armstrong or not using recursive
#function.

def count(n):
    if n==0:
        return 0
    else:
        return 1+count(n//10)
        
def armstrongNumber(n):
    if n==0:
        return 0
    else:
        d=n%10
        return d**c+armstrongNumber(n//10)
    
def isArmstrong(res,n):
    if res==n:
        return True
    else:
        return False

n=1535
c=count(n)
print(c)
res=armstrongNumber(n)
print(res)
check=isArmstrong(res,n)
print(check)

