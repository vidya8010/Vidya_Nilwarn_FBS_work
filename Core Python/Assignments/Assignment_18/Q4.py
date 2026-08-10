# 4. Remove all of the vowels in a string (take input from user)
s=input('Enter string:')
li=[i for i in s if i not in 'aeiouAEIOU']
ss=''.join(li)
print(ss)