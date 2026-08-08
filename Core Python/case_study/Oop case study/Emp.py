from abc import ABC,abstractmethod

class Emp(ABC):
    def __init__(self,id,name,sal):
        super().__init__()
        self.id=id
        self.name=name
        self.sal=sal
    @abstractmethod
    def calsal():
        pass
    def __str__(self):
        return f'id={self.id} name={self.name} sal={self.sal}'
    def __repr__(self):
        return super().__str__()