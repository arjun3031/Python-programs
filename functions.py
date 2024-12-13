# def my_function():
#     print("Hello World")
# my_function()

def fun1(a,b):
    print(a+b)
fun1(10,20)

#Arbitory arguments
def fun2(*a):
    print(a[3])
fun2(1,2,3,5)

#Keyword arguments
def fun3(a,b,c):
    print(b)
fun3(a=10,b=20,c=30)

#Arbitory keyword arguments
def fun4(**a):
    print(a["fname"])
fun4(fname="Arjun",lname="K M")

#Default parameter
def fun5(country="India"):
    print(country)
fun5("USA")
fun5("Germany")
fun5()

