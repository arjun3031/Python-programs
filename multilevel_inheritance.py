import datetime

d=datetime.datetime.now()
date=d.strftime("%Y: %h: %d")
print("")
print("MULTILEVEL INHERITANCE"," [ Date -",date," ]")
print("")

class person:
    def __init__(self):
        self.fname=input("Enter Your First Name: ")
        self.lname=input("Enter Your Last Name: ")
        self.age=int(input("Enter Your Age: "))

    def show(self):
        print("")
        print("   Personal Details")
        print("First Name: ",self.fname)
        print("Last Name: ",self.lname)
        print("Age: ",self.age)

class department(person):
    def __init__(self):
        person.__init__(self)
        self.did=int(input("Enter Department ID: "))
        self.dname=input("Enter Department Name: ")
        self.place=input("Enter Department Location: ")

    def show(self):
        super().show()
        print("Department ID: ",self.did)
        print("Department Name: ",self.dname)
        print("Department Location: ",self.place)

class employee(department):
    def __init__(self):
        department.__init__(self)
        self.eid=int(input("Enter Employee ID: "))

    def show(self):
        super().show()
        print("Employee ID: ",self.eid)

obj=employee()
obj.show()

        