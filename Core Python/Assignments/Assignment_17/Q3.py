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
class MedicalStudent(Student):

    def __init__(self,studentId,name,age,percentage,specialization, marksOfInternship):
        super().__init__(studentId, name,age, percentage)
        self.specialization = specialization
        self.marksOfInternship = marksOfInternship

    def Accept(self):
        super().Accept()
        self.specialization = input("Enter Specialization: ")
        self.marksOfInternship = float(input("Enter Marks Of Internship: "))

    def Display(self):
        super().Display()

        print("Specialization:", self.specialization)
        print("Marks Of Internship:", self.marksOfInternship)

    def CalculateRank(self):
        total = self.percentage + self.marksOfInternship

        if total >= 150:
            return "Distinction"
        elif total >= 120:
            return "First Class"
        elif total >= 100:
            return "Second Class"
        elif total >= 70:
            return "Pass Class"
        else:
            return "Fail"

    def __str__(self):
        return (f"ID: {self.studentId}, "
                f"Name: {self.name}, "
                f"Age: {self.age}, "
                f"Percentage: {self.percentage}, "
                f"Specialization: {self.specialization}, "
                f"Internship Marks: {self.marksOfInternship}")