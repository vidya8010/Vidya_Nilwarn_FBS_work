#Write a program to input any alphabet and check whether it is vowel or consonant.
char=input('Enter aplhabet:')
if char in 'aeiouAEIOU':
    print(f'{char} is vowel')
else:
    print(f'{char} is consonant')