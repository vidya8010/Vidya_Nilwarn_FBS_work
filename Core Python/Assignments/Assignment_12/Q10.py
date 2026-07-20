#10.Python Program to Take in Two Strings and Display the Larger String
#without Using Built-in Functions
def largerString(s1,s2):
    c1=0
    c2=0
    for i in s1:
        c1+=1
    for j in s2:
        c2+=1
    if c1>c2:
        return s1
    else:
        return s2
s1=input('Enter str1:')
s2=input('Enter str2:')
print(largerString(s1,s2))