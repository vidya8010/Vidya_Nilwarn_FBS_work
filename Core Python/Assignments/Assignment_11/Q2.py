#Python Program to Merge Two Lists and Sort it
def selectionsort(li):
    size=len(li)
    for i in range(size-1):
        min=i
        for j in range(i+1,size):
            if li[j]<li[min]:
                min=j
        li[i],li[min]=li[min],li[i]

def mergeList(li1,li2):
    li1.extend(li2)
    selectionsort(li1)
    return li1

li1=[1,2,5,6,3,4]
li2=[6,7,5,3,3]
li4=mergeList(li1,li2)
print(li4)