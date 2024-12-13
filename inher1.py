print("Simple inheritance \n")
print("")

class cal:
    def __init__(self,n1,n2):
        self.n1=n1
        self.n2=n2
    def add(self):
        print("Sum is: ",self.n1+self.n2)
    def sub(self):
        print("Sub is: ",self.n1-self.n2)
    def mul(self):
        print("mul is: ",self.n1*self.n2)
    def div(self):
        if self.n2>0:
            print("div is: ",self.n1/self.n2) 
        else:
            print("No division taken place")  
n1=int(input("Enter the first number: "))
n2=int(input("Enter the second number: "))
obj=cal(n1,n2)
obj.add()
obj.sub()
obj.mul()
obj.div()


        