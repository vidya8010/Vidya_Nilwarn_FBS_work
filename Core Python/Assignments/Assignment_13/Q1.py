#Python Program to Add a Key-Value Pair to the Dictionary
def addKeyValPair(di,n):
    for i in range(n):
        val=input('Enter value:')
        di[i]=val
    return di

di={}
n=int(input('Enter how many pair you want:'))
print(addKeyValPair(di,n))