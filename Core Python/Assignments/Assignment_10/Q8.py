#Write a program to create a duplicate of an existing list. It should not point to
# same list.
def duplicateList(li):
    li2=[]
    for i in li:
        li2.append(i)
    return li is li2
li=[1,2,3,4,5,6]
res=duplicateList(li)
print(res)
