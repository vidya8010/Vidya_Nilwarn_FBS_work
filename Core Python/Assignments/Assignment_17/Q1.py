# 1. Create a class Student with following
# a. data members :
# i. StudentId
# ii. Name
# iii. Age
# iv. Percentage
# b. Add the following methods :
# i. Parameterized constructor
# ii. Display
# iii. Accept
# iv. Method CalculateRank
# v. Override __str__ Method


class Student:
    def __init__(self,id=0,name='',age=0,per=0):
        self.id=id
        self.name=name
        self.age=age
        self.per=per
    def accept(self):
        self.id=int(input('Enter id:'))
        self.name=input('Enter name:')
        self.age=int(input('Enter age:'))
        self.per=float(input('Enter percentage:'))
    def display(self):
        print(
            f'\n id:{self.id}\n name:{self.name}\n age:{self.age}\n per:{self.per}'
        )
    def CalculateRank(self):
        if self.per >= 75:
            return "Distinction"
        elif self.per >= 60:
            return "First Class"
        elif self.per >= 50:
            return "Second Class"
        elif self.per >= 35:
            return "Pass"
        else:
            return "Fail"
    def __str__(self):
        return (f"Student ID: {self.id}\n"
                f"Name: {self.name}\n"
                f"Age: {self.age}\n"
                f"Percentage: {self.per}\n"
                f"Rank: {self.CalculateRank()}")

class EnggStudent:
    pass

s1=Student(101,'vidya',21,78)

#Using display function 
s1.display()

#accept data from student
s1.accept()

##using str
print(s1)