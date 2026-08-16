# 3. Create object of student class (Outside SY & TY package) having roll
# number, name, SYMakrs and TYMarks. Add the marksof SY and TY
# Computer subjects and calculate grade ("A" for >=70, "B" for >=60,
# "C" for >=50, “Pass Class” for >=40 else “Fail”) and display the result
# of the student in proper format.

from SyMArks.Q1 import SYMARKS
from TyMarks.Q2 import TYMARKS
class Student():
    def __init__(self,id,name,sy,ty):
        self.roll_no=id
        self.name=name
        self.sy=sy
        self.ty=ty
    def calculate(self):
        self.total = self.sy.computerTotal + self.ty.theory
        if self.total>70:
            self.grade='A'
        elif self.total>60:
            self.grade='B'
        elif self.total>50:
            self.grade='C'
        elif self.total>=40:
            self.grade='pass class'
        else:
            self.grade='Fail'
    def display(self):
        print("\n----- STUDENT RESULT -----")
        print("Roll No :", self.roll_no)
        print("Name    :", self.name)
        print("SY Computer :", self.sy.computerTotal)
        print("TY Theory   :", self.ty.theory)
        print("Total       :", self.total)
        print("Grade       :", self.grade)
sy=SYMARKS(67,40,30)
ty=TYMARKS(50,40)

s=Student(101,'vidya',sy,ty)
s.calculate()
s.display()
         