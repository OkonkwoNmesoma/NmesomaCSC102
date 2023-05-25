import random
class Employee():
    def check_employees(self):
        Employees = ['Mary Evans', 'Eyo Ishan', 'Durojaiye Dare', 'Adams Ali',
                     'Andrew Ugwu', 'Stella Mankinde', 'Jane Akibo', 'Ago James'
                     'Mitchell Taiwo', 'Abraham Jones', 'Nicole Anide','Kosi Korso',
                     'Adele Martins', 'Emmanuel Ojo', 'Ajayi Fatima']

        name = str.casefold(input("NAME: "))
        if name in Employees:
            print('hello')
            E.take_attendance()
            E.assign_task()
        else:
            E.refuse_access()
    def take_attendance(self):
        print("Welcome attendance has been checked")
    def assign_task(self):
        Tasks = {'Loading', 'Transporting', 'Reviewing Orders', 'Customer Service',
                 'Delivering Items'}
        print("Task is: ", random.randint(Tasks))
    def refuse_access(self):
        print("You are not a member of the organization")

E = Employee()
E.check_employees()