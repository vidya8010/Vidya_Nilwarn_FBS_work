#Python Program to Calculate the Number of Words and the Number of
#Characters Present in a String
def calWordsChar(s1):
    l=len(s1.split())
    count =0
    for ch in s1:
        if ch!=' ':
            count+=1
    return l,count
s1=input('Enter string:')
w,c=calWordsChar(s1)
print(f'Words:{w} and characters:{c}')