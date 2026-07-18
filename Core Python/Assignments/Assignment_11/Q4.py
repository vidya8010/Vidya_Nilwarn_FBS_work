#Python Program to Find the Second Largest Number in a List Using Bubble
#Sort
def bubbleSort(li):
    size=len(li)
    for i in range(1,size):
        for j in range(0,size-i):
            if li[j]>li[j+1]:
                li[j+1],li[j]=li[j],li[j+1]

def secondLargest(li):
    largest = li[-1]
    for i in range(len(li) - 2, -1, -1):
        if li[i] != largest:
            return li[i]
    return None

li=[2,4,6,3,4,6,6,6]
bubbleSort(li)
print(li)
sc=secondLargest(li)
print(sc)