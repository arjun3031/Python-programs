def common_letters():
    str1=input("Enter first string: ")
    str2=input("Enter second string: ")
    s1=set(str1)
    s2=set(str2)
    cmn=s1 & s2
    print("Common letter is: ",cmn)
common_letters()