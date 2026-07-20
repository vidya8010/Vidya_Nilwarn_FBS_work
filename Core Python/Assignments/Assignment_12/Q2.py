#Python Program to Remove the nth Index Character from a Non-Empty String
def removeChar(s,n):
    if 0<=n<len(s):
        res=s[:n]+s[n+1:]
        print(f'After removing character string is ',res)
    else:
        print('Invalid input')
s=input('Enter the string:')
n=int(input('Enter index from which you have to remove charater:'))
removeChar(s,n)


