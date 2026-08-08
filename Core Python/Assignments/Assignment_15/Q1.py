#1. Create a class Book with members as bid,bname,price and author.Add following
# methods:
# a. Constructor (Support both parameterized and parameterless)
# b. Destructor
# c. ShowBook

class Book:
    def __init__(self,bid=0,bname=' ',price=0):
        self.bid=bid
        self.bname=bname
        self.price=price
    def getId(self):
        return self.bid
    def setId(self,bid):
        self.bid=bid
    def getName(self):
        return self.bname
    def setname(self,bname):
        self.bname=bname
    def getPrice(self):
        return self.price
    def setPrice(self,p):
        self.price=p
    def ShowBook(self):
        print(f'bid={self.bid}\t bname={self.bname}\t price={self.price}')

    def __del__(self):
        print('object deleted')


b=Book(101,'Shyamchi Aai',350)
b.ShowBook()