# Dictionary

d1={"Name":"Arjun","Age":23,"Year":2024}
print(d1)
print(d1["Name"])

#Value Fetch using get()
print(d1.get("Age"))

d1["Year"]=2025
print(d1)

for i in d1.values():
    print(i)
print(len(d1))


d1["Place"]="Calicut"

#Removing Name
d1.pop("Name")
print(d1)

#Removing last item
d1.popitem()
print(d1)

#Deleting Particular Key
del d1["Age"]
print(d1)

#Update
d2={"Last_name":"K M","Course":"Python"}
d1.update(d2)
print(d1)

#Multiple Dictionary
d={
    "Child1":{"Name":"Abhi","Age":23},
    "Child2":{"Name":"Aju","Age":24,"Place":"Kochi"},
    "Child3":{"Name":"Deepu","Age":25}
}
print(d["Child2"]["Place"])