print("Factorial of a number")
print("")

n=int(input("Enter the number: "))
f=1
i=1
while i<=n:
    f=f*i
    i=i+1
print("Factorial of ",n," is ",f)
