#13 . Write a program to print list after removing even numbers.
def removeEnven(li):
    new_list=[]
    for i in range(len(li)):
        if i%2!=0:
            new_list.append(i)
    return new_list
li=[1,2,3,4,5,6,7]
res=removeEnven(li)
print(res)