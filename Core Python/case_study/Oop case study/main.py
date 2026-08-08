from employeemanage import Empmanagement

def login():
    em=Empmanagement()
    uid=input('Enter user id:')
    password=input('Enter password:')
    if uid=='admin' and password=='123':
        while True:
            print('Please select 1 option from below') 
            print('1.Add')
            print('2.display')
            print('3.search')
            print('4.update')
            print('5.delete')
            choice=int(input('Enter choice:'))
            if choice==1:
                em.AddEmp()
            elif choice == 2:
                em.DisplayEmp()
            elif choice == 3:
                em.SearchEmp()
            elif choice==4:
                em.UpdateEmp()
            elif choice == 5:
                em.DeleteEmp()
            elif choice == 6:
                print('visit again')
            else : 
                print('Wrong choice entered')
    else:
        print('Invalid id and password')
login()
