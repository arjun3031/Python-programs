#Lambda Function used for creating anonymous function multiple expression at a time
x=lambda a:a*a
print(x(5))

y=lambda a,b:a+b
print(y(2,4))

z=lambda a,b,c:a*b/c
print(z(2,3,4))

def fun(a):
    x=a*a
    print(x)
fun(5)