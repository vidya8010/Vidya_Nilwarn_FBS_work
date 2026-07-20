#Write a Python program to find the longest common prefix of all
#strings. Use the Python set.
def longPreffix(st):
    smallest = min(st,key=len)
    l=len(smallest)
    pr=''
    for i in range(l):
        chars = set()
        for s in st:
            chars.add(s[i])
        if len(chars) == 1:
            pr += st[0][i]
        else:
            break
    print("Longest Common Prefix:", pr)

st=['start','star','stop','sit']
longPreffix(st)

