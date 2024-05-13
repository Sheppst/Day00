def RevAlph() :
    a = ""
    for i in range(97,123,1) :
        a += chr(i)
        print (a)
    for i in range(1,len(a)+1):
        b = ""
        print(b)
        print(i)
        print(a[-i])
        b += a[-i]
    print (b)

RevAlph()
