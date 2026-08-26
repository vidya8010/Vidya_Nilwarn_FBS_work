# 1. Create a class Emp (eid,ename,basic)
# 2. WAP a menu driven program to perform following operations using
# files :

# a. Add a record
# b. Search for a record using id
# c. Delete a record using id
# d. Edit a record using id.
# e. Display all records.
class Emp:
    def __init__(self,eid,name,basic_sal):
        self.eid=eid
        self.name=name
        self.basic_sal=basic_sal

def add():
    pass
def search():
    pass
def delete():
    pass
def edit():
    pass
def display():
    pass


while True:

    print("\n===== Employee Management =====")
    print("1. Add Record")
    print("2. Search Record")
    print("3. Delete Record")
    print("4. Edit Record")
    print("5. Display All Records")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        add()

    elif choice == 2:
        search()

    elif choice == 3:
        delete()

    elif choice == 4:
        edit()

    elif choice == 5:
        display()

    elif choice == 6:
        print("Program ended")
        break

    else:
        print("Invalid choice")