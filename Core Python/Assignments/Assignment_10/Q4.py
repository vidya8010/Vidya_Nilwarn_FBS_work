#Write a program to reverse the list.
def reverseList(li):
    right=0
    left=len(li)-1
    while right<left:
        li[right],li[left]=li[left],li[right]
        right+=1
        left-=1
    return li
li=[4,5,6,7,8,9,10]

print(reverseList(li))