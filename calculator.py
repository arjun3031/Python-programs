def cal():
    print("1. ADD")
    print("2. SUB")
    print("3. MUL")
    print("4. DIV")
    print("5. MOD")
    print("6.EXIT")
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    while True:
        c = int(input("Enter your choice: "))
        if c == 1:
            add = a + b
            print("Sum is", add)
        elif c == 2:
            sub = a - b
            print("Difference is", sub)
        elif c == 3:
            mul = a * b
            print("Multiplication is", mul)
        elif c == 4:
            div = a / b
            print("Division is", div)
        elif c == 5:
            mod = a % b
            print("Modulas is", mod)
        elif c == 6:
            print("Exit")
            break
        else:
            print("Invalid choice")
cal()
