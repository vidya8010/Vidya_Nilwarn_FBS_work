# 1. A list contains the denominations as follows :
# D = [2000, 500, 200, 100 , 50, 20, 10, 5]
# Accept an amount from user and calculate how many
# minimum number of notes will be needed for that
# amount.

# D = [2000, 500, 200, 100 , 50, 20, 10, 5]


D=[2000, 500, 200, 100, 50, 20, 10, 5]
amount=int(input("Enter the amount: "))
dictt={}
count=0
for note in D:
    if amount>=0:
        notes=amount//note
        count+=notes
        amount=amount%note
        dictt[note]=count
print(dictt)
print("Minimum number of notes needed:", count)
    