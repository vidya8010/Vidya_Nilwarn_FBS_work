from Hr import Hr
from devoper import Dev
class Empmanagement:
    empdata = { }

    def AddEmp(self):
        print("------------Add Employee----------")
        emp_id = int(input("Enter Id:"))
        if emp_id in self.empdata:
            print("Employee already exist...")
            return
        else:
            name = input("Enter Employee name:")
            sal = float(input("Enter salary:"))
            print("1.Hr")
            print("2.Trainer")
            ch = int(input("Select one:"))
            if ch == 1:
                com = float(input("Enter commision:"))
                emp = Hr(emp_id,name,sal,com)

            elif ch == 2:
                bonus = float(input("Enter bonus:"))
                emp = Dev(emp_id,name,sal,bonus)
            else:
                print("Invalid Input")
                return
            Empmanagement.empdata[emp_id] = emp
            print("Employee Added Successfully......")
        

    def DisplayEmp(self):
        if Empmanagement.empdata:
            for emp in Empmanagement.empdata.values():
                print(emp)
        else:
            print('No record available')
        
    def SearchEmp(self):
        id=int(input('Enter id to search record:'))
        if id in self.empdata:
            print(Empmanagement.empdata[id])
        else:
            print(f'{id} is not present.2')
    def UpdateEmp(self):
        print("---- Update Employee ----")
        emp_id = int(input("Enter id: "))

        if emp_id in Empmanagement.empdata:
            emp = Empmanagement.empdata[emp_id]
            print('1.Name')
            print('2.Salary')
            ch=int(input('Choose what you want to update:'))
            
            if ch==1:
                emp.name = input("Enter new name: ")
                print("Employee name updated successfully.")
            elif ch==2:
                emp.salary=float(input('Enter new salary:'))
                print("Employee salary updated successfully.")
            else:
                print('Entered wrong choice')
        else:
            print("Employee ID does not exist.")
            

    def DeleteEmp(self):
        print("---- Delete Employee ----")

        emp_id=int(input("Enter id: "))

        emp=Empmanagement.empdata.pop(emp_id,None)

        if emp:
            print("Employee deleted successfully.")
        else:
            print("Employee ID does not exist.")
    def Exit(self):
        print("Thank you for visit")
