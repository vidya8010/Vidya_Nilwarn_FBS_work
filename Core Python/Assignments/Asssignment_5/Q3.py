#Accept no. of passengers from user and per ticket cost. Then accept age of each
#passenger and then calculate total amount to ticket to travel for all of them based on
#following condition :
#a. Children below 12 = 30% discount
#b. Senior citizen (above 59) = 50% discount
#c. Others need to pay full.

num=int(input('Enter how many passenger:'))
ticket_a=float(input('Enter ticket amount as per user:'))
total_ticket_am=0
for pass_no in range(1,num+1):
    print(f'Age of {pass_no}')
    age=int(input('Enter age:'))
    if(age<12):
        final_tk=ticket_a-(30/100)*ticket_a
    elif(age>59):
        final_tk=ticket_a-(50/100)*ticket_a
    else:
        final_tk=ticket_a
    total_ticket_am+=final_tk
print(f'Total ticket amount of {num} passengers is {total_ticket_am}')