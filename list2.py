# Create two list to store even and odd numbers from the first list

ls1=[]
n=int(input("Enter the size of list: "))
for i in range(1,n+1):
    a=int(input(f"Enter the Element {i}: "))
    ls1.append(a)
print("Created list is: ",ls1)
ls2=[]
ls3=[]
for i in ls1:
    if i%2==0:
        even=ls2.append(i)
    else:
        odd=ls3.append(i)
print("Even numbers from the list: ",ls2)
print("Odd numbers from the list: ",ls3)