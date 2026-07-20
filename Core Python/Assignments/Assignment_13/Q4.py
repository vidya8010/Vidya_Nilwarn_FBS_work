#Python Program to Generate a Dictionary that Contains Numbers (between 1
#and n) in the Form (x,x*x).
def genDict(d1,n):
    for i in range(1,n+1):
        d1[i]=i*i
    return d1
n=int(input('Enter n:'))
di={}
print(genDict(di,n))