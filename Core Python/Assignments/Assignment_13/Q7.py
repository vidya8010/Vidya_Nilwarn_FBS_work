#Python Program to Remove the Given Key from a Dictionary
def removeKey(di, key):
    if key in di:
        di.pop(key)
        return di
    else:
        return "Key not found"

di = {1: 'a', 2: 'b', 3: 'c'}
key = int(input("Enter key to remove: "))

print(removeKey(di, key))