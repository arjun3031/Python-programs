def words_count():
    str=input("Enter the string: ")
    li=str.split()
    d={}

    for i in li:
        if i not in d.keys():
            d[i]=0
        d[i]=d[i]+1
    print(d)
words_count()
    