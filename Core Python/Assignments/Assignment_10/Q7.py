#7. Write a program to create a new list from existing list which contains cube of
#each number of list.
def cubList(li):
    li2=list(map(lambda i:i**2,li))
    return li2
li=[1,2,3,4,5]
cube_lis=cubList(li)
print(cube_lis)