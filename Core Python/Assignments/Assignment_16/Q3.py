# 3. Create a class Shirt with members as sid,sname,type(formal etc), price and
# size(small,large etc) .Add following methods:
# j. Constructor (Support both parameterized and parameterless)
# k. Destructor
# l. ShowBook
# m. For each size of shirt price should change by 10%.
# (eg. If 1000 is price then small price = 1000, medium = 1100,large=1200 and
# xlarge=1300) Use static concept.


class Shirt:
    # Static variable
    base_price=1000

    def __init__(self,sid=0,sname="",stype="",size="small"):
        self.sid=sid
        self.sname=sname
        self.stype=stype
        self.size=size.lower()

    def __del__(self):
        print("Shirt object destroyed.")

   
    def ShowBook(self):

        if self.size=="small":
            price=Shirt.base_price
        elif self.size=="medium":
            price=Shirt.base_price + Shirt.base_price * 10 / 100
        elif self.size=="large":
            price=Shirt.base_price + Shirt.base_price * 20 / 100
        elif self.size == "xlarge":
            price=Shirt.base_price + Shirt.base_price * 30 / 100
        else:
            price=Shirt.base_price

        print("\nShirt ID   :", self.sid)
        print("Shirt Name :", self.sname)
        print("Type       :", self.stype)
        print("Size       :", self.size)
        print("Price      :", price)



s1=Shirt(101,"Peter England","Formal","small")
s2=Shirt(102,"Levis","Casual","medium")
s3=Shirt(103,"Arrow","Formal","large")
s4=Shirt(104,"Van Heusen","Party Wear","xlarge")

s1.ShowBook()
s2.ShowBook()
s3.ShowBook()
s4.ShowBook()
    