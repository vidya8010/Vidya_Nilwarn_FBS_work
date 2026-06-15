#Convert the time entered in hh,min and sec into seconds.

#Take input
h=int(input('Enter hours:'))
m=int(input('Enter minutes:'))
s=int(input('Enter seconds:'))

#Perform operation 
seconds=h*3600+m*60+s

#Display result
print(f'Total seconds are {seconds}')