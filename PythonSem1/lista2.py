from random import randint

global chance
chance = 0
#Zadanie 1

def szachownica(n,k):
    k*=2
    for i in range(0,k):
        if i % 2 != 0:
            for j in range(0,n):
                for l in range(0,k):
                    if l % 2 == 0:
                        for p in range(0,n):
                            print("* ",sep='', end='')
                    else:
                        for p in range(0,n):
                            print("  ",sep='', end='')
                print()
        else:
            for j in range(0,n):
                for l in range(0,k):
                    if l % 2 == 0:
                        for p in range(0,n):
                            print("  ",sep='', end='')
                    else:
                        for p in range(0,n):
                            print("* ",sep='', end='')
                print()
szachownica(0,0)


def graSmoka():
    ciagi = ["el:5: zaleznosc:>:","el:6: zaleznosc:>=:","el:10: zaleznosc:!=:","el:5: zaleznosc:<:"] 
    #print("Zostales zchwytany przez smoka. Wybierz ciag (1,2,3...) z nastepujacych ktory da ci wolnosc jezeli pojawi sie w wylosowanych 100 liczbach.")
    #for i in range(len(ciagi)):
        #print(str(i+1) + ". " + ciagi[i])

    #print()
    #wybranyCiag = input(": ")
    wybranyCiag = 4
    
    #print("Wybrales " + str(wybranyCiag) + " ciag")
    wybranyCiag = int(wybranyCiag)-1
    #print()
    #print("Losowanie 100 liczb...")
    losowaneLiczby = []
    for j in range(100):
        losowaneLiczby.append(randint(0,6))
    #print(losowaneLiczby)
    szukanieCiagu = []
    poczatekCiagu = 0
    szukanieCiagu.append(losowaneLiczby[0])
    wybranyciagf = ciagi[int(wybranyCiag)].split(":")[3]
    i = 1
    while True:
        #print("i:",i+1)
        #print("Poczatek:",poczatekCiagu+1)
        if i>=100:
            #print("You are still stuck!")
            print(0)
            break
        elif len(szukanieCiagu) == int(ciagi[int(wybranyCiag)].split(":")[1]):
            #print(szukanieCiagu)
            #print("Jestes wolny!")
            print(1)
            global chance
            chance += 1
            break
        elif eval(("losowaneLiczby[i] " + wybranyciagf + " szukanieCiagu[len(szukanieCiagu)-1]")):
            szukanieCiagu.append(losowaneLiczby[i])
            
            #print("i:",i+1,"current:",losowaneLiczby[i])
            i+=1
        else:
            i=poczatekCiagu+1
            if i>=100:
                #print("You are still stuck!")
                print(0)
                break
            poczatekCiagu += 1
            #print("i:",i+1,"current:",losowaneLiczby[i])
            #print(szukanieCiagu)
            szukanieCiagu = list()
            szukanieCiagu.append(losowaneLiczby[poczatekCiagu])
            #print(szukanieCiagu)
            i+=1

for k in range(1000):
    graSmoka()

print(chance)