#2. Write a program to find maximum and minimum element in a list.
def maxMin(li):
    max=li[0]
    min=li[0]
    for i in range(len(li)):
        if li[i]>max:
            max=li[i]
        else:
            min=li[i]
    return max,min
li=[1,2,3,4,5,6,7,8]
max,min=maxMin(li)
print('Maximum number:',max)
print('minimum number:',min)