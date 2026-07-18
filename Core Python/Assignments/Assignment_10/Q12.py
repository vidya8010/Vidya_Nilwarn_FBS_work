#Write a program to create three lists of numbers, their squares
#and cubes

def createList(li):
    n=int(input('Enter length of your list:'))
    for i in range(0,n):
        i=int(input('Enter element:'))
        li.append(i)
    return li
def square(li2):
    li3=list(map(lambda x:x**2,li2))
    return li3
def cubes(li2):
    li4=list(map(lambda i:i**3,li2))
    return li4

li=[]
li2=createList(li)
print(li2)
li3=square(li2)
print(li3)
li4=cubes(li2)
print(li4)