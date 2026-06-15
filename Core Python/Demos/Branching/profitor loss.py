#Profit or loss

#Take input
cp=int(input('Enter cost price:'))
sp=int(input('Enter selling price:'))
#Find profit and loss
p=sp-cp
# l=cp-sp

#Check the condition 
if p>0:
    print(f'profit is {p}')
elif p==0:
    print('No loss no profit')
else:
    print(f'loss of {p}')