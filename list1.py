#Sum of elements in a list

def ls():
    list=[]
    n=int(input("Size of list: "))
    for i in range(1,n+1):
        a=int(input(f"Enter the Element {i}: "))
        list.append(a)
    s=sum(list)
    print("Sum of numbers in the list is: ",s)
ls()