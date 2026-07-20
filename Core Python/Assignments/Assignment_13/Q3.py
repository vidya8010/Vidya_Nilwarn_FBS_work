#3. Python Program to Check if a Given Key Exists in a Dictionary or Not
def checkKey(di,key):
    if key in di:
        return True
    else:
        return False
d1={1:'a',2:'b',3:'c'}
key=int(input('Enter key:'))
print(checkKey(d1,key))