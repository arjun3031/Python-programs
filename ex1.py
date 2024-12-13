l1=[]
l2=[]
l3=[]
print("1.Simple Swapping")
print("2.Third Variable")
print("3.Length of list")
while True:
    x=int(input("Enter your choice: "))
    if x==1:
        n=int(input("Enter the size of list: "))
        for i in range(1,n+1):
            a=int(input(f"Enter element {i}: "))
            l1.append(a)
        print("Before swapping: ",l1)
        print("First element: ",l1[0])
        print("Last element: ",l1[-1])
        if n>1:
            l1[0],l1[-1]=l1[-1],l1[0]
            print("After swaping: ",l1)
        else:
            print("List must contain more than one item")
    elif x==2:
        n=int(input("Enter the size of list: "))
        for i in range(1,n+1):
            b=int(input(f"Enter the element {i}: "))
            l2.append(b)
        print("Before Swap: ",l2)
        r=l2[0]
        l2[0]=l2[-1]
        l2[-1]=r
        print("After Swap: ",l2)
    elif x==3:
        n=int(input("Enter the size of list: "))
        for i in range(1,n+1):
            a=int(input(f"Enter element {i}: "))
            l3.append(a)
        print("Lenth: ",len(l3))
    else:
        print("Invalid Choice")
        break
        
