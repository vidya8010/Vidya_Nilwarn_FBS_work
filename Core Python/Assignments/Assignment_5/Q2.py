#Enter number of students from user. For those many students accept marks of 5
#subject marks from user and calculate percentage. Display all percentage and
#average percentage of students.
num=int(input('Enter how many students:'))
avg_sum=0
avgper=0
for i in range(1,num+1):
    print(f'Roll number of student is {i}')
    total=0
    for j in range(1,6):
        m=int(input('Enter marks student with roll number:'))
        total+=m
    per=total/5
    avg_sum+=per
    print(f'percentage of student with Roll number {i} is {per}%')
avgper=avg_sum/num
print(f'Average percebtage of student is {avgper}')




