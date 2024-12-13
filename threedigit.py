def threedig():
    dig=input("Enter the three digit number: ")
    if len(dig)!=3:
        print("Not a three digit number")
        return
    a=int(dig[0])
    b=int(dig[1])
    c=int(dig[2])
    if a%2==0:
        print("First digit is even") 
    else:
        print("First digit is odd")

    if b%2==0:
        print("second digit is even") 
    else:
        print("second digit is odd")

    if c%2==0:
        print("third digit is even") 
    else:
        print("third digit is odd")
threedig()