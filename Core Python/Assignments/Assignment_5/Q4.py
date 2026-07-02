#4. WAP to print Armstrong number within a given range
start=int(input('Enter starting:'))
end=int(input('Enter ending'))
for i in range(start,end):
    temp=i
    count=0
    arm_num=0
    while temp>0:
        count+=1
        temp//=10
    temp=i
    while temp>0:
        digit=temp%10
        arm_num+=(digit**count)
        temp//=10
    if i==arm_num:
        print(i)
