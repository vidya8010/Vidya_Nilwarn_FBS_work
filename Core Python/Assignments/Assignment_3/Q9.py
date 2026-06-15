#Input 5 subject marks from user and display grade(eg.First class,Second class ..)
m1=int(input('Enter marks of sub1:'))
m2=int(input('Enter marks of sub2:'))
m3=int(input('Enter marks of sub3:'))
m4=int(input('Enter marks of sub4:'))
m5=int(input('Enter marks of sub5:'))

per=((m1+m2+m3+m4+m5)/500)*100

if(per>90):
    print('passes with first class')
elif(per>70):
    print('passed with second class')
else:
    print('passed with third class')