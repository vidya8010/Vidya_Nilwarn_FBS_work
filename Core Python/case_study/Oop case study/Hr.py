from Emp import Emp
class Hr(Emp):
    def __init__(self,id,name,sal,com):
        super().__init__(id, name, sal)
        self.com=com
    def calsal(self):
        return self.sal+self.com
        
    def __str__(self):
        return f'id:{self.id}\t name:{self.name}\t sal:{self.calsal()}'
    def __repr__(self):
        return self.__str__()