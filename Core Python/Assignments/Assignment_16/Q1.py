# Create a class Book with members as bid,bname,price and author.Add following
# methods:
# a. Constructor (Support both parameterized and parameterless)
# b. Destructor
# c. ShowBook
# d. Add static variable count and also maintain count of objects created.


class Book:
    count=0

    @staticmethod
    def getCount():
        return Book.count

    @staticmethod
    def setCount():
        Book.count+=1
    
    def __init__(self,bid,bname,price,author):
        self.bid=bid
        self.bname=bname
        self.price=price
        self.author=author
        Book.setCount()

    def getId(self):
        return self.bid
    def setId(self,bid):
        self.bid=bid
    def getName(self):
        return self.bname
    def setName(self,bname):
        self.bname=bname
    def getPrice(self):
        return self.price
    def setPrice(self,p):
        self.price=p
    def getAuthor(self):
        return self.author
    def setAuthor(self,author):
        self.author=author

    def showBook(self):
        print(f'bid:{self.bid}\t name:{self.bname}\t price:{self.price}\t Author:{self.author}')

    def __del__(self):
        print(f'I am destructor')


b=Book(101,'Shyamchi Aai',340,'Sane Guruji')
b.showBook()
b1=Book(102,'Swami',560,'Shivaji sawant')
b1.showBook()

print(Book.count)