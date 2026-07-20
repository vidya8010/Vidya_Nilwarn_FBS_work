#Python Program to Form a New String where the First Character and
#the Last Character have been Exchanged
def newString(s1):
    if len(s1) <= 1:
        return s1
    s2 = s1[-1] + s1[1:-1] + s1[0]
    return s2
s1='vidya'
print(newString(s1))
