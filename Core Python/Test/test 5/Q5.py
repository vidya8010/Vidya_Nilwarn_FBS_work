# 5. Python Program to Find the Union of two Lists without
# using set concept.

li1=[1,2,3,4,5]
li2=[6,7,8,8,2,3,1]
li3=[]
for i in li1:
    if i not in li3:
        li3.append(i)
for j in li2:
    if j not in li3:
        li3.append(j)
print(li3)