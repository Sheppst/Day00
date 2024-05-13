def RevAlph() :
    a = ""
    for i in range(97,123,1) :
        a += chr(i)
    for i in range(len(a)):
        b += a[-i]
    print (b)

RevAlph()
