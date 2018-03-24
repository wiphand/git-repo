class ListItem:
    def __init__(self,value):
        self.val = value
        self.next = None


lista = ListItem(2)
lista.next = ListItem(3)
lista.next.next = ListItem(4)

def naKoniec(lis):
    while lis.next!=None:
        lis = lis.next
    lis.next = ListItem(4)

def wypisz(lis):
    while lis!=None:
        print (lis.val)
        lis = lis.next
naKoniec(lista)
wypisz(lista)
print (lista.next.val)