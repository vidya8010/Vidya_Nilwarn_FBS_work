# 6. Use a dictionary comprehension to count the length of each word
# in a sentence (take input from user)
s=input('Enter string:')
dic={i:len(i) for i in s.split()}
print(dic)  