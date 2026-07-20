#Python Program to count number of digits and letters in a string.
def calDigChar(s1):
    cn=0
    cc=0
    for i in s1:
        if i.isdigit():
            cn+=1
        elif i.isalpha():
            cc+=1
        else:
            print('not digit not digit')
    return cn,cc

s1='vidya123'
cn,cc=calDigChar(s1)
print(f'digits:{cn} and characters:{cc}')