# Create a class Student with following
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
    def __init__(self, studentId,name,age,percentage):
        self.studentId=studentId
        self.name=name
        self.age=age
        self.percentage=percentage

    def Accept(self):
        self.studentId=int(input("Enter Student ID: "))
        self.name=input("Enter Name: ")
        self.age=int(input("Enter Age: "))
        self.percentage=float(input("Enter Percentage: "))

    def Display(self):
        print("Student ID:",self.studentId)
        print("Name:",self.name)
        print("Age:",self.age)
        print("Percentage:",self.percentage)
        print("Rank:",self.CalculateRank())

    def CalculateRank(self):
        if self.percentage>=75:
            return "Distinction"
        elif self.percentage>=60:
            return "First Class"
        elif self.percentage>=50:
            return "Second Class"
        elif self.percentage>=35:
            return "Pass Class"
        else:
            return "Fail"

    def __str__(self):
        return f"ID: {self.studentId}, Name: {self.name}, Age: {self.age}, Percentage: {self.percentage}"

class EnggStudent(Student):

    def __init__(self, studentId, name, age, percentage, branch, internalMarks):
        super().__init__(studentId, name, age, percentage)
        self.branch=branch
        self.internalMarks=internalMarks

    def Accept(self):
        super().Accept()
        self.branch=input("Enter Branch: ")
        self.internalMarks=float(input("Enter Internal Marks: "))

    def Display(self):
        super().Display()
        print("Branch:",self.branch)
        print("Internal Marks:",self.internalMarks)

    def CalculateRank(self):
        total = self.percentage + self.internalMarks

        if total>=150:
            return "Distinction"
        elif total>=120:
            return "First Class"
        elif total>=100:
            return "Second Class"
        elif total>=70:
            return "Pass Class"
        else:
            return "Fail"

    def __str__(self):
        return f"ID: {self.studentId}, Name: {self.name}, Age: {self.age}, Percentage: {self.percentage}, Branch: {self.branch}, Internal Marks: {self.internalMarks}"

e1 = EnggStudent(101,"Rahul",20,75,"Computer", 20)
e1.Display()
print(e1)
