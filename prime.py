a=int(input("Enter the starting range: "))
b=int(input("Enter the Ending range: "))
print("Prime numbers are: ")
for i in range(a,b+1):
    if i>1:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print(i)