start = int(input("Starting Number: "))
end = int(input("Ending Number: "))
armstrong_numbers = []
for i in range(start, end + 1):
    a = len(str(i))
    s = 0
    c = i
    for j in range(a):
        b = c % 10
        s += b ** a
        c //= 10  
    if s == i:
        armstrong_numbers.append(i)

print("Armstrong numbers between",start,"and",end,"are",armstrong_numbers)

