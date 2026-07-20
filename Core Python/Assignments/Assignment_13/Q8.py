#Python Program to Count the Frequency of Words Appearing in a String Using
#a Dictionary
def freqWord(d1,s1):
    s2=s1.split()
    for i in s2:
        d1[i]=s2.count(i)
    return d1
d1={}
s1=input('Enter a string:')
print(freqWord(d1,s1))