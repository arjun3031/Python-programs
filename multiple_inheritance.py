class person:
    def __init__(self):
        self.fname=input("Enter First Name: ")
        self.lname=input("Enter Last Name: ")

    def show(self):
        print("Fist Name: ",self.fname)
        print("Fist Name: ",self.lname)

class department:
    def __init__(self):
        self.did=int(input("Enter department ID: "))
        self.dname=input("Enter department Name: ")

    def show(self):
        print("department ID: ",self.did)
        print("department Name: ",self.dname)

class student(person,department):
    def __init__(self):
        person.__init__(self)
        department.__init__(self)
        self.id=int(input("Enter student ID: "))

    def show(self):
        person.show(self)
        department.show(self)
        print("Student ID: ",self.id)
        

obj=student()
obj.show()
    