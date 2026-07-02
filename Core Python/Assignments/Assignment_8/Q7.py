#7. Write a program to find sum of digits of a number.
def digitSum(n):
    temp=n
    sum=0
    while temp>0:
        digit=temp%10
        sum+=digit
        temp//=10
    print(f'Summation of digits is {sum}')

n=int(input('Enter number:'))
digitSum(n)