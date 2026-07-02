#8. Write a program find reverse of a number
def revNumber(n):
    temp=n
    rev=0
    while temp>0:
        digit=temp%10
        rev=rev*10+digit
        temp//=10
    print(f'Reverse number of {n} is {rev}')
n=int(input('Enter number:'))
revNumber(n)

