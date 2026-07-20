#Python Program to Remove the Characters of Odd Index Values in a String
def removeOddIndex(s1):
    l=len(s1)
    return s1[0:l:2]

s=input('enter string:') 
print(removeOddIndex(s))