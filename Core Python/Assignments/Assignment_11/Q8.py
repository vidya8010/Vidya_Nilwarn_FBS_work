# #Print 1 to 100 in snakes and ladder pattern.

li=list(range(1,101))
start=0
end=10
li2=[]
for i in range(10):
    nes_li=li[start:end]
    if i%2==1:
        nes_li=nes_li[::-1]
    li2.append(nes_li)
    start=end
    end=end+10
for j in li2[::-1]:
    print(j)
# print(li2)
    

