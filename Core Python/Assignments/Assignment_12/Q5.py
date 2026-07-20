#Python Program to Count the Number of Vowels in a String
def countVowel(s):
    count=0
    for i in s:
        if i in'aeiouAEIOU':
            count+=1
    return count
s=input('Enter string:')
print(countVowel(s))