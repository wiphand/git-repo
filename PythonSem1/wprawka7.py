import itertools
def wygeneruj(monety,n):
    wynik=[]
    for i in itertools.combinations_with_replacement(monety,n):
        wynik+= [''.join(i)]
    return wynik

def rozmien(suma,monety):
    string = ''.join(str(x) for x in monety)
    for i in range(suma//monety[0]+1):
        ##print(str(monety))
        w = wygeneruj(string,i)
        for j in range(len(w)):
            #print('+'.join(w[j]))
            temp=sum(int(x) for x in w[j] if x.isdigit())
            ##temp = eval('+'.join(temp2))
            if(temp==suma):
                print('+'.join(w[j])) 

rozmien(5,[1,2,5])