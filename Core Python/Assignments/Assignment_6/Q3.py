for i in range(1,6):
    k=1
    for j in range(1,6-i):
        print(' ',end='')
    for j in range(1,i+1):
        if j==1 or i==j:
            print(k,end=' ')
        else:
            print(i-1,end=' ')
    print()