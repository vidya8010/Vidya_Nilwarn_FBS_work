#Python Program to Calculate the Length of a String Without Using a
#Library Function
def stringLength(s1):
    count=0
    for i in s1:
        count+=1
    return count
s=input('Enter string : ')
print(stringLength(s))