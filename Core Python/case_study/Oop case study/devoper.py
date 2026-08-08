from Emp import Emp
class Dev(Emp):
    def __init__(self,id,name,sal,ins):
        super().__init__(id, name, sal)
        self.ins=ins
    def calsal(self):
        return self.sal +self.ins
    def __str__(self):
        return f'\t id:{self.id}\t name:{self.name}\t sal:{self.calsal()}'
    def __repr__(self):
        return self.__str__()
    