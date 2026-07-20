#Python Program to Take in a String and Replace Every Blank Space
#with Hyphen
def replaceBlank(s):
    s2=s.replace(' ','-')
    return s2
s=input('Enter string : ')

print(replaceBlank(s))