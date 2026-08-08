class Student:
    def __init__(self,studentId,name,age,percentage):
        self.studentId=studentId
        self.name=name
        self.age=age
        self.percentage=percentage

    def __str__(self):
        return f"ID: {self.studentId}, Name: {self.name}, Age: {self.age}, Percentage: {self.percentage}"

class College:
    def __init__(self, numberOfStudents):
        self.numberOfStudents=numberOfStudents
        self.students=[]

    def AddStudent(self,student):
        if len(self.students) < self.numberOfStudents:
            self.students.append(student)
            print("Student added successfully.")
        else:
            print("College is full.")

    def GetStudent(self,studentId):
        for student in self.students:
            if student.studentId==studentId:
                return student

        return None

    def RemoveStudent(self,studentId):
        student = self.GetStudent(studentId)

        if student is not None:
            self.students.remove(student)
            print("Student removed successfully.")
        else:
            print("Student not found.")

    def __str__(self):
        result = "----- College Students -----\n"

        for student in self.students:
            result+=str(student) + "\n"

        return result

college=College(3)

s1=Student(101, "Rahul", 20, 80)
s2=Student(102, "Amit", 21, 75)

college.AddStudent(s1)
college.AddStudent(s2)

print(college)

student=college.GetStudent(101)

if student is not None:
    print("Found:",student)

college.RemoveStudent(102)

print(college)