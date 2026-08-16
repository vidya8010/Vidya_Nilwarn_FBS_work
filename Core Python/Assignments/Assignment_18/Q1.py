#1. Create a class Complex Number with data members as real and imag and add
# following methods :
# a. Constructor
# b. Destructor
# c. Overload +,- operator
class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __del__(self):
        print("Destructor called")

    def __add__(self, c):
        return Complex(self.real + c.real, self.imag + c.imag)

    def __sub__(self, c):
        return Complex(self.real - c.real,self.imag - c.imag)

    def display(self):
        print(self.real, "+", self.imag, "i")


c1 = Complex(10,20)
c2 = Complex(5,10)

c3 = c1 + c2
c4 = c1 - c2

print("Addition:")
c3.display()

print("Subtraction:")
c4.display()