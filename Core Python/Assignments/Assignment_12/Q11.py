#Python Program to replace every blank space with hyphen in a string.

def replaceBlank(s):
    return s.replace(' ','-')

s=input('Enter string : ')
print(replaceBlank(s))