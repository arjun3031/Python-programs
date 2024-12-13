
print("DICTIONARY OPEARATIONS")
print("")

print("1.CREATE")
print("2.SEARCH")
print("3.PRINT")
print("""4.UPDATE 
  a)Only value
  b)Both key and value
  c)Change all data
  d)Add new key and values""")
print("5.DELETE")
print("6.CLEAR DATA")
print("6.EXIT")
print("")

d={}
dictionary_created=False
while True:
    n=int(input("Enter your choice: "))
    print("")
    if n==1:
        x=int(input(f"Enter number of pairs: "))
        for i in range(x):
            y=input(f"Enter key {i+1}: ")
            z=input(f"Enter value {i+1}: ")
            d[y]=z
        dictionary_created=True
        print("Dictionary created")
        print("")
    elif n==2:
        if dictionary_created:
            p=input("Enter the key to search: ")
            q=input("Enter the value to search: ")
            if p in d and d[p]==q:
                print("Search pair exists")
                print("")
            else:
                print("Search pair does not exist")
                print("")
        else:
            print("Dictionary not found")
    elif n==3:
        if dictionary_created:
            print("Created dictionary is: ",d)
            print("")
        else:
            print("Dictionary not found.You must create a dictionary first")
    elif n==4:
        if dictionary_created:
            k=input("Enter your sub choice: ")
            print("")
            if k=='a':
                print("Only value to update")
                j=input("Enter the key: ")
                if j in d:
                    h=input("Enter new value: ")
                    d[j]=h
                    print("Updated dictionary is: ",d)
                    print("")
                else:
                    print("key does not exist")
                    print("")
            elif k=='b':
                print("Both key and value update")
                l=input("Enter the key: ")
                if l in d:
                    u=input("Enter new key: ")
                    v=input("Enter new value: ")
                    d[u]=v
                    del d[l]
                    print("Updated dictionary is: ",d)
                    print("")
                else:
                    print("Key does not exist")
                    print("")
            elif k=='c':
                print("Change all data")
                o=int(input("Enter the new size: "))
                d2={}
                for i in range(1,o+1):
                    p=input(f"Enter new key {i}: ")
                    q=input(f"Enter new value {i}: ")
                    d2[p]=q
                d=d2
                # d.update(d2)
                print("Updated dictionary is: ",d2)  
                print("")
            elif k=='d':
                print("Add new key & value")
                o=int(input("Enter the new size: "))
                if o==x:
                    print("Same size as old dictionary")
                else:
                    d2={}
                    for i in range(1,o+1):
                        p=input(f"Enter new key {i}: ")
                        q=input(f"Enter new value {i}: ")
                        d2[p]=q
                    d.update(d2)
                    print("Updated dictionary is: ",d2)  
                    print("")
            else:
                print("Invalid choice")
                print("")
        else:
            print("Dictionary not found")
    elif n==5:
        if dictionary_created:
            del d
            print("Dictionary is deleted")
        else:
            print("Dictionary not found")
    elif n==6:
        if dictionary_created:
            d.clear()
            print("Data in dictionary is cleared")
        else:
            print("Dictionary not found")
    elif n==7:
        print("Exit")
        break
    else:
        print("Invalid choice")
        print("")



