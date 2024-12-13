# class Person:
#     def __init__(self,fname,lname):
#         self.fname=fname
#         self.lname=lname
#     def display(self):
#         print(self.fname+" "+self.lname)
#         # print(self.lname)
# obj=Person("Arjun","KM")
# obj.display()

class car:
    def __init__(self):
        # self.cname=cname
        # self.rate=rate
        # self.speed=speed
        # self.color=color
        self.cname=input("Enter the cname: ")
        self.rate=int(input("Enter the rate: "))
        self.speed=int(input("Enter the speed: "))
        self.color=input("Enter the color: ")
    def show(self):
        print(self.cname+" "+self.rate+" "+self.speed+" "+self.color)
obj1=car("Benz","1 CR","100","Blue")
obj1.show()