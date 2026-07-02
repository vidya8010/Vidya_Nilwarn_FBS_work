#9. Write a program to check if entered number is a palindrome or not.
def palindrome(n):
    temp=n
    rev=0
    while n>0:
        digit=n%10
        rev=rev*10+digit
        n//=10
    if rev==temp:
        print(f'{temp} is palindrome number')
    else:
        print(f'{temp} is not palindrome number')
n=int(input('Enter number:'))
palindrome(n)