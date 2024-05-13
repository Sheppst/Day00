def RevAlph() :
    a = ""
    for i in range(97,123,1) :
        a += chr(i)
    while a != "" :
        b += a[-1]
        del a[-1]
    print (b)

RevAlph()
