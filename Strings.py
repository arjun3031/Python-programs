a="Hello World"
print(a)

#Multiple line string
b="""Hello
good afternoon"""
print(b)

#printing based on index number
print(a[3])

#foor in string
for i in a:
    print(i)

#Count the space also in len()
print(len(a))

if "q" in a:
    print("Yes")
else:
    print("No")

#slicing
print(a[0:3])
print(a[:8])
print(a[2:])
print(a[-4:-7])

#Negative Index
print(a[-2])

#upper and lowercase
print(a.upper())
print(a.lower())

#replace
print(a.replace("Hellow","Hi"))

#concatination
c="Good evening"
print(a+" "+c)

#String formating
age=24
text="My name is Arjun, I'm "+str(age)
print(text)

text="My name is Arjun, I'm {}"
print(text.format(age))

print(f"My age is {age}")

'''price=100
text="The price is {}"
print(text.format(price))'''
