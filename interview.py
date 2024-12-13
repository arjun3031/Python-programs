import datetime
from collections import Counter

x=datetime.datetime.now()
a=x.strftime("%d: %b: %Y")
print(a)
print("")

print("Interview Question")
print("")

#method 2
l1=[]
l2=[]
n=int(input("Enter the size of first string: "))
for i in range(1,n+1):
    c=input(f"Enter the charecter {i} in first String: ")
    l1.append(c)
print("")
m=int(input("Enter the size of second string: "))
for i in range(1,m+1):
    d=input(f"Enter the charecter {i} in second String: ")
    l2.append(d)
print("")
if n==m:
    print("Size of first String == Size of second String") 
    l1.sort()
    l2.sort()
    if l1==l2:
        print("Charecters are same in both Strings")
        print("Charecters in both Strings are: ",l1)
    else:
        print("Different charecters in both Strings")    
else:
     print("Both Strings must have same size")

#method 2
# s1=input("Enter first string: ")
# s2=input("Enter second string: ")
# c1=Counter(s1)
# c2=Counter(s2)
# if c1==c2:
#     print("All characters are equal")
# else:
#     print("Different Characters")