#Date and Time

import datetime

x=datetime.datetime.now()
print(x)

# #For Displaying Year,Month
print(x.year)
print(x.month)


# y="20 June 2023"
# z=datetime.datetime.strttime(y,"%d %B %y")
# print(z)

# a=x.strftime("%B")
# print(a)

# a=x.strftime("%m")
# print(a)

# a=x.strftime("%d")
# print(a)

# a=x.strftime("%h:%M:%S")
# b=x.strftime("%h ,%M ,%S")
c=x.strftime("%a")
# print(a,b)
print(c)