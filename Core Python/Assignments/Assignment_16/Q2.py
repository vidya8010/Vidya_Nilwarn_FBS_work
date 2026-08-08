# Create a class Product with members as pid,pname,price and quantity .Add
# following methods:
# e. Constructor (Support both parameterized and parameterless)
# f. Destructor
# g. ShowBook
# h. Add static member discount.
# i. Provide methods for applying discount on price of product.

class Product:
    discount=10
    @staticmethod
    def applyDis(p):
        dis=p-(p*Product.discount/100)
        return dis

    def __init__(self,pid=0,pname=' ',price=0,quantity=' '):
        self.pid=pid
        self.pname=pname
        self.price=price
        self.quantity=quantity

    def getId(self):
        return self.pid
    def setId(self,id):
        self.pid=id
    def getName(self):
        return self.pname
    def setName(self,name):
        self.pname=name
    def getPrice(self):
        return self.price
    def setPrice(self,price):
        self.price=price
    def getQuantity(self):
        return self.quantity
    def setQuantity(self,q):
        self.quantity=q
    def showProduct(self):
        print(f' id={self.pid}\t pname={self.pname}\t price={Product.applyDis(self.price)}\t quantity={self.quantity}')  

    def __del__(self):
        print('Destructor called') 
    
p1=Product(101,'Food',450,'3kg')
p1.showProduct()
