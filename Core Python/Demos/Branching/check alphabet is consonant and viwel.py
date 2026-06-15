#check weather the character is vowel or consonant

#take Input 
alpha=input('Enter char:')
#Check condition 
if alpha in 'aeiouAEIOU':
    #if condition is true then print
    print(f'{alpha} is vowel')
else:
    #if condition is false then print
    print(f'{alpha} is consonant')