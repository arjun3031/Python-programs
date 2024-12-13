t1=("Mango","Apple","Banana")
print(t1)
print(len(t1))

#If in tuple
if "Magno" in t1:
   print("Present")
else:
   print("Not Present")

#Add element using List
l1=list(t1)
l1[2]="Graps"
t1=tuple(l1)
print(t1)

#Adding element By using append()
l1.append("Graps")
t1=tuple(l1)
print(t1)

#Removing element using List and remove()
l2=list(t1)
l2.remove("Apple")
t1=tuple(l2)
print(t1)

#Multiple tuple operation
t2=(1,2,3,7)
t3=3*t2+t1
print(t3)

#Type of Tuple element
t2=(True,)
print(type(t2))

