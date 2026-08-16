# Find all of the words in a string that are less than 5 letters (take
# input from user)
s=input('Enter string:')
ss=s.split()
li=[i for i in ss if len(i)<5]
print(li)