import random as r

def OrderIntTab ():
    tab = []
    for i in range(15):
        a = 0
        a = r.randint()
        tab.append(a)
    for i in range (len(tab)) :
        for j in range (0 , len(tab) - i - 1) : 
            if tab[j] > tab[j+1]:
                tab[j], tab[j+1] = tab[j+1], tab[j]
    print (tab)

OrderIntTab() 


