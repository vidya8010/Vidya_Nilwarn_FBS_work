#11. Write a program to accept an integer amount from user and tell minimum number of notes needed for representing that amount.

#Take input

A=int(input('Enter amount:'))

#Perform operation 

# notes=[2000,1000,500,200,100,50,20,10,5,2,1]
# for i in range(0,len(notes)):
#     if a>=notes[i]:
#         c=a//notes[i]
#         dictt[notes[i]]=c
#     a=a%notes[i]

#Display result
# print(dictt)

n1=A//2000
print('2000 rs notes are ',n1)

A=A%2000
if A>1000:
    n2=A//1000
else:
    n2=A//500
