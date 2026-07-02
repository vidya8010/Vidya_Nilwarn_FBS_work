#WAP to check if a given number is Armstrong number or not. For
#each task create separate functions.
def checkStatus(n):
    if n>0:
        return n
    else:
        return None
    
def countDigit(n):
    temp=n
    count=0
    while temp>0:
        count+=1
        temp//=10
    return count

def digitSeparate(n,c):
    new_no=0
    while n>0:
        digit=n%10
        new_no+=digit**c
        n//=10
    return new_no

def checkArmstromg(n,new_no):
    if n==new_no:
        print(f'Number is Armstrong')
    else:
        print(f'Number is not armstrong')

n=int(input('Enter n:'))
num=checkStatus(n)
if num is not None:
    #If number is positive then send this number to digit counting
    c=countDigit(num)
    #Send this number and count to digit separate out and calculate armstrong
    new_no=digitSeparate(num,c)
    #check that number and new_no is same or not
    checkArmstromg(num,new_no)
else:
    print(f'Please enter positive number')



