#Search an element from the list
import datetime
x=datetime.datetime.now()
y=x.strftime("%Y:%h:%d")
z=x.strftime("%H: %M")
print(y,"  ",z)
print("")

print("List Operations")
print("")
print("1.CREATE A LIST")
print("2.APPEND DATA")
print("3.SEARCH DATA")
print("4.DELETE DATA")
print("5.VIEW LIST")
print("6.EXIT")
while True:
    print("")
    a=int(input("Enter Your Choice: "))
    print("")
    if a==1:
        print("Creating List")
        list=[]
        print("Your List is Created with Empty elements")
    elif a==2:
        print("Inserting Data")
        n=int(input("Enter the size of List: "))
        for i in range(1,n+1):
            a=input(f"Enter element {i} to Insert: ")
            list.append(a)
        print("Created list is: ",list)
    elif a==3:
        print("Seraching from List")
        b=input("Enter the element to be search: ")
        if b in list:
            p=list.index(b)
            print(f"Searched {b} is found at postion {p}")
        else:
            print(f"Searched {b} is not found")
    elif a==4:
        print("Removing from List")
        r=input("Enter the Element to Remove: ")
        if r in list:
            list.remove(r)
            print(f"{r} is Removed from the List")
        else:
            print(f"{r} is Not a Valid Data from the List")
    elif a==5:
        print("Viewing List")
        print("Your List is: ",list)
    elif a==6:
        print("Existing")
        break
    else:
        print("Invalid Choice")

        