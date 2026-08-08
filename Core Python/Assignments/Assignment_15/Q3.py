# 3. Create a class Shirt with members as sid,sname,type(formal etc), price and
# size(small,large etc) .Add following methods:
# g. Constructor (Support both parameterized and parameterless)
# h. Destructor
# i. ShowBook

class Shirt:
    def __init__(self,sid,sname,type,size):
        self.sid=sid
        self.sname=sname
        self.type=type
        self.size=size
    def getId(self):
        return self.sid
    def setId(self,sid):
        self.sid=sid
    def getName(self):
        return self.sname
    def setname(self,name):
        self.sname=name
    def getType(self):
        return self.type
    def setType(self,type):
        self.type=type
    def getSize(self):
        return self.size
    def setSize(self,size):
        self.size=size
    def showbox(self):
        print(f'sid={self.sid}\t sname={self.sname}\t Stype={self.type}\t Size={self.size}')

s1=Shirt(101,'Raymond','Formal','XXL')
s1.showbox()