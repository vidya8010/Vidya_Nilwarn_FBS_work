#Python Program to Find the Intersection of Two Lists
def intersectionList(li1,li2):
    li3=[]
    for i in li1:
        if i in li2 and i not in li3:
            li3.append(i)
    return li3

li=[1,2,3,4,5]
li1=[4,2,2,5,6,7]
i_list=intersectionList(li,li1)
print(f'Internsection list:',i_list)
