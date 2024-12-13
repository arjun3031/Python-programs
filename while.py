#while(if using break)
i=1
while i<10:
    print(i)
    if i==5:
        break
    i=i+1

#while(contiue)
i=0
while i<5:
    i=i+1
    if i==3:
        continue
    print(i)