print("Fibonacci Series")
a=0
b=1
n=int(input("Number of series: "))
for i in range(n):
    print(a)
    c=a+b
    a=b
    b=c
if n==0:
    print("No series found")

    