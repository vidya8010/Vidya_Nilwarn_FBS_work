import pickle
class Emp:
    def __init__(self, eid, ename, basic):
        self.eid = eid
        self.ename = ename
        self.basic = basic
    def display(self):
        print(self.eid, self.ename, self.basic)
while True:
    print("\n1. Add Record")
    print("2. Search Record")
    print("3. Delete Record")
    print("4. Edit Record")
    print("5. Display All Records")
    print("6. Exit")
    ch = int(input("Enter choice: "))
    # Add Record
    if ch==1:
        eid=int(input("Enter ID: "))
        ename=input("Enter Name: ")
        basic=float(input("Enter Basic: "))
        e=Emp(eid,ename,basic)
        with open("emp.dat","ab") as f:
            pickle.dump(e,f)
        print("Record added")
    # Search Record
    elif ch == 2:
        eid = int(input("Enter ID to search: "))
        found = False
        with open("emp.dat", "rb") as f:
            try:
                while True:
                    e=pickle.load(f)
                    if e.eid==eid:
                        e.display()
                        found=True
                        break
            except EOFError:
                pass
        if not found:
            print("Record not found")
    # Delete Record
    elif ch==3:
        eid=int(input("Enter ID to delete: "))
        records=[]
        with open("emp.dat", "rb") as f:
            try:
                while True:
                    e=pickle.load(f)
                    if e.eid!=eid:
                        records.append(e)
            except EOFError:
                pass
        with open("emp.dat", "wb") as f:
            for e in records:
                pickle.dump(e,f)
        print("Record deleted")
    # Edit Record
    elif ch==4:
        eid=int(input("Enter ID to edit: "))
        records=[]
        with open("emp.dat", "rb") as f:
            try:
                while True:
                    e=pickle.load(f)
                    if e.eid==eid:
                        e.ename=input("Enter new name: ")
                        e.basic=float(input("Enter new basic: "))
                    records.append(e)
            except EOFError:
                pass

        with open("emp.dat", "wb") as f:
            for e in records:
                pickle.dump(e,f)
        print("Record updated")
    # Display All Records
    elif ch==5:
        with open("emp.dat", "rb") as f:
            try:
                while True:
                    e=pickle.load(f)
                    e.display()
            except EOFError:
                pass
    # Exit
    elif ch==6:
        break
    else:
        print("Invalid choice")