#Accept a number from user and check if this element is present in the list or
#not. Also tell how many times it is present in the list.

def elemntSearch(li,num,c):
    for i in li:
        if i==num:
            c+=1
    if c==0:
        return -1
    else:
        return c
num=int(input('Enter number:'))
li=[10,20,56,78,87,20,20]
c=0
res=elemntSearch(li,num,c)
if res==-1:
    print('Elemnt is not present in list')
else:
    print(f'{num} is avalable {res} times')
