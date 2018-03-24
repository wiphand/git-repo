from __future__ import division
import itertools

wejscie="3$3"
x=50
zestaw="+-*/"

def podstaw(wartosc, zamiana):
    for i in range(len(zamiana)):
        wartosc=wartosc.replace("$",zamiana[i],1)
    return wartosc

def wygeneruj(n):
    wynik=[]
    iter=0
    temp=""
    for i in itertools.product(zestaw,repeat=n):
        wynik+= [''.join(i)]
    return wynik
        
for i in range(len(wygeneruj(wejscie.count('$')))):
    if(eval(podstaw(wejscie,wygeneruj(wejscie.count('$'))[i]))==x):
        print("Wynik:",podstaw(wejscie,wygeneruj(wejscie.count('$'))[i]), "=",x)
