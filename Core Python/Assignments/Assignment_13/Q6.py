#Python Program to Multiply All the Items in a Dictionary
def proItems(di):
    m=1
    for val in di.values():
        m*=val
    return m
di={1:4,2:8,3:12}
print(proItems(di))