#Write a program to calculate the percentage of student based on marks of any 5 subjects.

#take input
m1=int(input('Enter m1:'))
m2=int(input('Enter m2:'))
m3=int(input('Enter m3:'))
m4=int(input('Enter m4:'))
m5=int(input('Enter m5:'))

#Perform Operation 
obtained_m=m1+m2+m3+m4+m5
# total_m=500
per=(obtained_m/500)*100

#Display result
print(f'Percentage of student with best 5 criteria is {per}')