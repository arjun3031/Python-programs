class Person:
    def __init__(self):
        self.fname=input("Enter first Name: ")

    def show(self):
        print(self.fname)

class Employee(Person):
    def __init__(self):
        Person.__init__(self) #for rerun person class
        self.salary=int(input("Enter the Salary: "))

    def show1(self):
        super().show()
        print(self.salary)
obj=Employee()
obj.show1()