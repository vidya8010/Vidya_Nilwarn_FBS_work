for i in range(1,6):
    for j in range(1,6-i):
        print(' ',end=' ')
    for j in range(1,i+1):
        if i==1 or j==1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    for j in range(1,i):
        if i==j+1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
for i in range(1,6):
    for j in range(1,i):
        print(' ',end=' ')
    for j in range(i,6):
        if i==j:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    for j in range(1,6-i):
        if i==5-j:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
