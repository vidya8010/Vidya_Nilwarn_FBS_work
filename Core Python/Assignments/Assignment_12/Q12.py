#Python Program to count number of lowercase characters in a string.
def calLower(s1):
    count=0
    for i in s1:
        if i.lower():
            count+=1
    return count
s1=input('Enter string:')
print(calLower(s1))