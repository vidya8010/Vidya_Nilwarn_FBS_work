c=64
for i in range(1,6):
    for j in range(1,6-i):
        print(' ',end=' ')
    for j in range(i,0,-1):
        print(chr(c+(i-j+1)),end=' ')
    for j in range(1,i):
        print(chr(c+j+i),end=' ')
    print()