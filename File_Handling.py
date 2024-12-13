#File Handling -  CREATE, UPDATE, READ, WRITE, CLOSE

# f=open("arjun.txt","r")

#Display first 4 Charecters including space

# print(f.read(4))
# print(f.readline())
# f.close()

#File Create

# f=open("myfile.txt","x")
# print("File Create")

#Append and Write into a File
# f=open("myfile.txt","a")
# f.write("My Name is Arjun")
# f=open("myfile.txt","r")
# print(f.read())
# f.close()

# f=open("myfile.txt","w")
# f.write("Over written")
# f=open("myfile.txt","r")
# print(f.read())
# f.close()

import os
if os.path.exists("myfile.txt"):
    os.remove("arjun.txt")
    print("File removed")
else:
    print("File Does'nt Exist")