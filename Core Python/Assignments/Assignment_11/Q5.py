#Python Program to Sort a List According to the Length of the Elements
#within the list.

li=['apple','chiku','pineapple','seeds','tea']
for i in range(len(li)-1):
    small=i
    for j in range(i+1,len(li)):
        l2=len(li[j])
        if len(li[j]) < len(li[small]):
            small=j
    li[i],li[small]=li[small],li[i]
        
print(li)