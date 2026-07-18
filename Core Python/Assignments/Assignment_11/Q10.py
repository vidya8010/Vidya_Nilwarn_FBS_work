def removeEven(li):
    li2=[]
    for i in li:
        if i%2!=0:
            li2.append(i)
    return li2

li=[1,2,3,4,5,6,7,8,9]

result=removeEven(li)
print(result)