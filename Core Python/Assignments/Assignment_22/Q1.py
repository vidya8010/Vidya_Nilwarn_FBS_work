class Emp:
    def __init__(self, eid, ename, basic):
        self.eid = eid
        self.ename = ename
        self.basic = basic


with open("emp.txt", "a") as f:
    eid = input("Enter ID: ")
    ename = input("Enter Name: ")
    basic = input("Enter Basic Salary: ")
    f.write(eid+" "+ename+" "+basic+"\n")

with open("emp.txt", "r") as f:
    for line in f:
        data = line.split()
        e = Emp(data[0], data[1], data[2])
        print("ID:", e.eid)
        print("Name:", e.ename)
        print("Basic:", e.basic)