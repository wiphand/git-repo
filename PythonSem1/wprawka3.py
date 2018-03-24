"""Napisz funkcję który dla danego słowa v i pliku z listą słów zwróci zbiór z wszystkimi słowami w których występuje v.
Następnie wykorzystaj funkcję do napisania procedury, która dla danych 3 słow [x,y,z] zwróci(powinieneś zrealizować każdy wariant):
-zbiór słów z danego pliku w których występuje każde z x,y,z
-zbiór słów z danego pliku w których występuje co najmniej jedno z x,y,z
-zbiór słów z danego pliku w których występuje co dokładnie jedno z x,y,z(tzn. jeśli w słowie występuje x, to żadne nie może występować, ponadto jedno z tych trzech musi)
-zbiór słów z danego pliku w których występuje x, ale nie występuje z
-zbiór słów z danego pliku dla których jest spełniony warunek: (x występuje w słowie => y występuje w słowie)

Wszystkie warianty powinny być napisane z użyciem operacji na zbiorach(np. sumy, różnicy itp.)

"""
import re

def getZbior(podciag):
    file1 = open("slowa.txt","r", encoding='utf-16-le')
    snew = set()
    while(True):
        s = file1.readline()
        s = s.strip()
        #print(
        if(s == ""):
            break
        if(podciag in s):
            snew.add(s)
    #print(snew)
    file1.close()
    return snew
    
print(getZbior("sp") & getZbior("pi") & getZbior("la"))

print((getZbior("las") ^ getZbior("flag")) ^ getZbior("mas"))

print((getZbior("las").difference(getZbior("flag"))).difference(getZbior("mas")) | (getZbior("flag").difference(getZbior("las"))).difference(getZbior("mas"))|(getZbior("mas").difference(getZbior("flag"))).difference(getZbior("las")))

print(getZbior("las") - getZbior("mas"))

print((getZbior("las") ^ getZbior("flag")) ^ (getZbior("flag")-getZbior("las")) ^ ((getZbior("")-getZbior("flag"))&(getZbior("")-getZbior("las"))))

print(getZbior("")-(getZbior("las")^(getZbior("")-getZbior("flag"))))
