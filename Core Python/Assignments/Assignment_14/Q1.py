#1. Write a Python program to find elements in a given set that are not in
#another set.
def differe(s1,s2):
    s1.difference_update(s2)
    return s1
s1={1,2,3,4,5,6}
s2={1,2,8,9}

print(differe(s1,s2))

