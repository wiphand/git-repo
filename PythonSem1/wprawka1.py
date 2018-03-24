def pivot(lista,dzielnik):
    a = []
    a.append([])
    a.append([])
    for i in range(len(lista)):
        if lista[i]<=dzielnik:
            a[0].append(lista[i])
        else:
            a[1].append(lista[i])
    return a

lista = [3,4,2,1,6,5]
#print(pivot(lista,3))

def multiPivot(lista,listaDzielnikow):
    c = []
    for i in range(len(listaDzielnikow)):
        print(lista)
        c.append(pivot(lista,listaDzielnikow[i])[0])
        print(pivot(lista,listaDzielnikow[i])[0])
        lista = pivot(lista,listaDzielnikow[i])[1]
    c.append(lista)
    print(lista)
    return c
print(multiPivot([3,4,2,1,6,5],  [2,4]))