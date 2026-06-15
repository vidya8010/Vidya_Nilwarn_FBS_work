#WAP to calculate total salary of employee based on basic, da=10% of basic, ta=12% of basic, hra=15% of basic.

#take input
basic_sal=float(input('Enter basic salary:'))
da=10
ta=12
hra=15
#Perform operations

tda=da/100*basic_sal
tta=ta/100*basic_sal
thra=hra/100*basic_sal

total_sal=basic_sal+tda+tta+thra

#Display result
print(f'Total salary is {total_sal}')