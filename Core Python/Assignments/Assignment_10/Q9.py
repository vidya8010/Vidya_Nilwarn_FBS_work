def evenOdd(li):
    li1=[]
    li2=[]
    for i in li:
        if i%2==0:
            li1.append(i)
        else:
            li2.append(i)
    return li1,li2

li=[1,2,3,4,5,6,7,8,9]
res1,res2=evenOdd(li)
print(f'even number list:{res1}')
print(f'Odd number list:{res2}')