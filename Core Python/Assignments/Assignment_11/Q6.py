#Python Program to Find the Union of two Lists
def unionList(li1,li2):
    li3=[]
    for i in li1:
         if i not in li3:
            li3.append(i)
    for j in li2:
         if j not in li3:
            li3.append(j)
        
    return li3

li1=[1,2,3,4,5]
li2=[3,2,4,5,6]
u_list=unionList(li1,li2)
print(u_list)