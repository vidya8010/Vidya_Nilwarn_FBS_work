#Python Program to Sum All the Items in a Dictionary
def sumItems(di):
    sum=0
    for val in di.values():
        sum+=val
    return sum
di={1:4,2:8,3:12}
print(sumItems(di))