#1. Write a program to find sum of all elements of list
def sum1(li):
    sum = 0
    for i in range(len(li)):
        sum+=li[i]
    return sum
li=[1,2,3,4,5,6,7]
print(sum1(li))