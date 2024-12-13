#Exception Hnadling - TRY BLOCK, EXCEPT BLOCK, ELSE BLOCK and FINALLY BLOCK

#Try and Except

x="Arjun"
try:
    print(x)
except(NameError):
    print("No variable declared")
except:
    print("An Exception Occured")


try:
    print("Somthing went wrong")
except:
    print("Nothing wrong")

try:
    print(x)
except:
    print("Somthing went wrong")
else:
    print("Nothing wrong")

try:
    print(x)
except:
    print("Somthing went wrong")
finally:
    print("Finished")