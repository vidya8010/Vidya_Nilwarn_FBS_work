#Write a Python program to remove the intersection of a second set
#with a first set.
def differ(s1,s2):
    s1.difference_update(s2)
    return s1

s1={10,20,30}
s2={34,30,40}
print(differ(s1,s2))