#Regular Expression

#Search() in RE
import re
str="The rain in Spain is 100 mm"
x=re.search("^The.*Spain$",str)
if x :
    print("We have a match")
else:
    print("No match")

#Find() in RE
y=re.findall("[a-m]",str)
z=re.findall("[p..n]",str)
p=re.findall("[S.*n]",str)

#For Numbers
q=re.findall("\d",str)

print(y)
print(z)
print(p)
print(q)

#Split()
r=re.split("\s",str,2)
print("r")

#Sub 
s=re.sub("\s",str)