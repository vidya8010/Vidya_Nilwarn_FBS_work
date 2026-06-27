#Write a program to check if given number is Armstrong number or not.
num=int(input('Enter num:'))
temp=num
count=0
while(temp>0):
    count+=1
    temp//=10
temp=num
new_no=0
while(temp>0):
    digit=temp%10
    new_no=new_no+digit**count
    temp//=10
if new_no==num:
    print(f'{num} is armstrong number')
else:
    print(f'{num} is not armstrong number')