#13. Write a program to input electricity unit charges and calculate total electricity bill
#according to the given condition:
#For first 50 units Rs. 0.50/unit
#For next 100 units Rs. 0.75/unit
#For next 100 units Rs. 1.20/unit
#For unit above 250 Rs. 1.50/unit
#An additional surcharge of 20% is added to the bill

u=float(input('Enter unit charges:'))
bill=0
if u<=50:
    bill=u*0.5
elif u<=150:
    bill=0.5*50 + (u-50)*0.75
elif u<=250:
    bill=0.5*50 + 0.75*100 + (u-150)*1.2
else:
    bill=0.5*50+100*0.75+100*1.2+(u-150)*1.5
print(bill)

bill_w_charges=bill+20/100*bill

print(f'Total electricity bill : {bill_w_charges}')
