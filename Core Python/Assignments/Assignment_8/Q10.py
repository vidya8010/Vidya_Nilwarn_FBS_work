#10. Write a program to check if entered year is a leap year or not.

def leapYear(y):
    if y%4==0:
        print(f'{y} is leap year.')
    else:
        print(f'{y} is not leap year.')
y=int(input('Enter year:'))
leapYear(y)