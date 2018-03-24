#Lista 9
from random import randint

#zadanie 1
#Wprawka 3 (PR, 29.11)
"""Napisz funkcję, która dla danej listy (dowolny) najdłuższy spójny podciąg rosnący. Wymyśl fajną nazwę dla tej funkcji.

Przykładowo, dla listy [1,2,3,4,5,0,6,7,8] funkcja powinna zwrócić [1,2,3,4,5]. Wprawka w tej wersji warta jest 0.99.

W wersji za 1.0 rezygnujemy z wymagania spójności podciągu (i, co za tym idze, wynikiem powinno być [1,2,3,4,5,6,7,8])"""


ciag = [1,2,3,4,5,0,6,7,8]
def dlugiCiag(ciag):
    najdCiag=[]
    tempCiag=[]
    for i in range(len(ciag)):
        tempCiag.append(ciag[i])
        for j in range(i+1,len(ciag)):
            if(tempCiag[-1]<ciag[j]):
                tempCiag.append(ciag[j])
        if(len(tempCiag)>len(najdCiag)):
            najdCiag=tempCiag
        tempCiag=[]
    return najdCiag

#print(dlugiCiag(ciag))

#Zadanie 4
import turtle


def recTurtle(turtle, krok, n):
    while n > 0:
        tmp = turtle.heading()
        turtle.lt(90)
        turtle.fd(krok)
        turtle.rt(90)
        turtle.fd(krok)
        recTurtle(turtle, krok / 2, n - 1)
        turtle.fd(-2 * krok)
        recTurtle(turtle, krok / 2, n - 1)
        turtle.fd(krok)
        turtle.rt(90)
        turtle.fd(2 * krok)
        turtle.rt(90)
        turtle.fd(krok)
        recTurtle(turtle, krok / 2, n - 1)
        turtle.fd(-2 * krok)
        recTurtle(turtle, krok / 2, n - 1)
        turtle.fd(krok)
        turtle.rt(90)
        turtle.fd(krok)
        n -= 1
        turtle.seth(tmp)

#ekran = turtle.Screen()
#turtle = turtle.Turtle()
#turtle.speed(40)
#recTurtle(turtle, 200, 5)

#Zadanie 5 a + b
import random

litery={}
file0 = open("slowa.txt","r", encoding='utf-16-le').read().splitlines()
#liste slow ktora dostalismy ma w sobie duze litery, jezeli nie chcemy brac ich pod uwage jako osobne litery urzywamy nastepujacej linijki (wolniejsze rozwiazanie)
file0 = [ x.lower() for x in file0 if len(x.lower()) == len(set(x.lower()))]
#jezeli chcemy zeby duze litery byly analizowane jako osobne litery urzywamy nastepujacej linijki (szybsze rozwiazanie)
#file0 = [ x for x in file0 if len(x) == len(set(x))]
def polAlfaBeton():
    usedLetters=[]
    zdanie = ""
    n=0
    file1=list(file0)

    while n < 30:
        myline =random.choice(file1)
        #myline=myline.lower()
        if(set(myline).isdisjoint(usedLetters)):
            zdanie+=myline+" "
            usedLetters+=list(myline)
            for letter in myline:
                #print(letter)
                
                litery[letter]=litery.setdefault(letter,0)+1
                file1 = [ x for x in file1 if letter not in x ]
        n+=1
        if(len(file1)==0):
            break
    print(zdanie)

for i in range(1000):
    polAlfaBeton()
values = {k: 1000-v for k, v in litery.items()}
print(values)