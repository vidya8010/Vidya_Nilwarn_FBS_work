#Python Program to count the occurrences of each word in a string.
def calOccuWord(s):
    s1=''
    for i in s:
        if i not in s1:
            s1=s1+i
    for j in s1:
        print(f'{j}:{s.count(j)}')

s1 = input("Enter string: ")
calOccuWord(s1)