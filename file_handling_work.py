#File Handling
import os
import datetime

d=datetime.datetime.now()
date=d.strftime("%Y:%h:%d")
time=d.strftime("%H:%M")
print("FILE HANDLING"," [ Date -",date,"  Time -",time," ]")
print("  1.CREATE FILE")
print("  2.ADD DATA")
print("  3.VIEW FILE")
print("  4.OVERWRITE")
print("  5.REMOVE FILE")
print("  6.EXIT")   

while True:
    print("")
    n=int(input("   Enter Your Choice: "))
    print("")
    if n==1:
        print("     Creating File")
        x=input("   Enter Your File Name: ")
        if os.path.exists(x):
            print("   File Already Exists")
        else:
            f=open(x,"x")
            print("   File Created")
            f.close()
    elif n==2:
        print("         Adding Data")
        x=input("   Enter Your File Name: ")
        if os.path.exists(x):
            p=input("   Enter the Content: ")
            if len(p)>10:
                f=open(x,"a")
                f.write(p)
                print("   Data Entered")
            else:
                print("   Please Enter at Least 10 Charecters")
        else:
            print("   File Not Exist")
    elif n==3:
        print("     Viewing File")
        x=input("   Enter the File Name: ")
        if os.path.exists(x):
            f=open(x,"r")
            print("   Content is: ",f.read())
        else:
            print("   File Not Exists")
    elif n==4:
        print("     Overwriting Data")
        x=input("   Enter the File Name: ")
        if os.path.exists(x):
            f=open(x,"w")
            o=input("   Enter New Content: ")
            f.write(o)
        else:
            print("   File Not Exists")
    elif n==5:
        print("     Removing File")
        x=input("   Enter Your File Name: ")
        if os.path.exists(x):
            os.remove(x)
            print("   File Removed")
        else:
            print("   File Not Exists")
    elif n==6:
        print("     Exiting")
        break
    else:
        print("   Invalid Choice")
