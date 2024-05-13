import random as r

def RevOrderIntTab ():
    tab = []
    RevTab = []
    for i in range(15):
        a = 0
        a = r.randint(0,100)
        tab.append(a)
    for i in range (len(tab)) :
        for j in range (0 , len(tab) - i - 1) : 
            if tab[j] > tab[j+1]:
                tab[j], tab[j+1] = tab[j+1], tab[j]
    for i in range (len(tab)) :
        RevTab.insert(0,tab[i])

    print (RevTab)

RevOrderIntTab() 
