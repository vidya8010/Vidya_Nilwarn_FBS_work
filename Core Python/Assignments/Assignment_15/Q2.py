#Create a class Product with members as pid,pname,price and quantity .Add
# following methods:
# d. Constructor (Support both parameterized and parameterless)
# e. Destructor
# f. ShowBook


class Product:
    def __init__(self,pid=0,pname=' ',price=0,quantity=''):
        self.pid=pid
        self.pname=pname
        self.price=price
        self.quantity=quantity
    def getId(self):
        return self.pid
    def setId(self,pid):
        self.bid=pid
    def getName(self):
        return self.pname
    def setname(self,pname):
        self.pname=pname
    def getPrice(self):
        return self.price
    def setPrice(self,p):
        self.price=p
    def getQuantity(self):
        return self.quantity
    def setQuantity(self,q):
        self.quantity=q
    def ShowBook(self):
        print(f'bid={self.pid}\t bname={self.pname}\t price={self.price}\t quantity:{self.quantity}')

    def __del__(self):
        print('object deleted')

p=Product(101,'Food',60,'2kg')
p.ShowBook()