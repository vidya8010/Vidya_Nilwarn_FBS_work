#Write a Python program to find the two numbers whose product is
#maximum among all the pairs in a given list of numbers. Use the
#Python set.
def maxPro(li1):
    s=set(li1)
    li=list(s)
    max_pro=1
    p1,p2=0,0
    for i in range(len(li)):
        for j in range(i+1,len(li)):
            pro=li[i]*li[j]
            if pro>max_pro:
                p1,p2=li[i],li[j]
                max_pro=pro
    print(f'max product:{max_pro} with pair {p1} and {p2}')

li1=[1,5,2,4,7,9,9,5,3]
maxPro(li1)
