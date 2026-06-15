#Write a program to convert days into years, weeks and days.
#input
days=int(input('Enter days:'))

#Perform operation 

# calculate year
year=days//365
rem_days=days%365

#calculate weeks
weeks=rem_days//7

#calculate days
only_days=rem_days%7

print(f'In {days} there is {year} year , {weeks} weeks and {only_days} days. ')