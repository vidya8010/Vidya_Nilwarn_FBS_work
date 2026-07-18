#Write a program to remove all occurrences of a given element in the list.
def removeOccurenceOfElement(li,num):
    new_li=[]
    for i in li:
        if i!=num:
            new_li.append(i)
    return new_li
num=int(input('Enter number:'))
li=[1,2,3,2,4,2,3,4,6,5,6]
res=removeOccurenceOfElement(li,num)
print(res)