#Write a program to print all numbers which are divisible by m and n in the
#list.

def divisibleEle(li,m,n):
    li2=[]
    for i in li:
        if i%n==0 and i%m==0:
            li2.append(i)
    return li2
n=int(input('Enter n:'))
m=int(input('Enter m:'))
li=[10,20,30,40,50,60]
res=divisibleEle(li,m,n)
print(res)