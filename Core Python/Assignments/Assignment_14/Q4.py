#Write a Python program that finds all pairs of elements in a list whose
#sum is equal to a given value.
def pairElement(gv,li):
    for i in range(len(li)):
        for j in range(i+1, len(li)):
            if li[i] + li[j] == gv:
                print(li[i], li[j])
gv=int(input('Enter targeted value:'))
li=[1,2,5,8,7,9,3,4]
pairElement(gv,li)

    
