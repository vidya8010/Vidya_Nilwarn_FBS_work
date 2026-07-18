#Write a program to remove duplicates from the list.
def removeDuplicate(li):
    li2=[]
    for i in range(len(li)):
        if li[i] not in li2:
            li2.append(li[i])
    return li2
li=[1,2,3,5,3,4,2,3,4]
list1=removeDuplicate(li)
print(list1)
