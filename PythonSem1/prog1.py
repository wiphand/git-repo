# -*- coding: utf-8 -*-

# ten brzydki komentarz powyżej umożliwia kodowanie używanie polskich znaków (kodowanie utf-8)
# konieczne w pythonie 2.x
# Kodowanie windowsowe nazywa się cp1250
# W Pythonie 2.x usuwamy nawiasy w instrukcji print, a ponadto
# zamiast: print("*", end="") piszemy 
#      print "*",

# po znaku "#" rozpoczyna się komentarz

from math import sqrt # pierwiastek kwadratowy
from losowanie_fragmentow import losuj_fragment

def potega(a,n):
   wynik = 1  # zmienna lokalna
   for i in range(n):
      wynik = wynik * a   # albo: wynik *= a
   return wynik
   
def kwadrat(n):
   for i in range(n):
      for j in range(n):   # pętla w pętli
         print ("*", end="")
      print()
      
def kwadrat2(n):
   for i in range(n):
      print (n * "#")      
  

def silnia(n):
      wynik = 1
      n += 1
      for i in range(1,n):
            wynik *= i
      return wynik
      

"""  Zadanie trzecie  """
def krzyzyk(n):
      n+=1
      for i in range(1,4):
            if i == 1 or i == 3:
                  for y in range(1,n):
                        for j in range(1,4):
                              for p in range(1,n):
                                    print("* ",sep='', end='')
                        print()
            elif i == 2:
                  for y in range(1,n):
                        for j in range(1,4):
                              if j == 2:
                                    for k in range(1,n):
                                          print("  ",sep='', end='')
                              elif j == 1 or j == 3:
                                    for p in range(1,n):
                                          print("* ",sep='', end='')
                              
                        print()


"""  Zadanie Czwarte  """  
def losuj_haslo(n):
      result = ""
      while len(result)<n:
            if len(result) >= (n-5):
                  reqFragm = losuj_fragment()
                  while len(reqFragm)!= (n-len(result)):
                        reqFragm=losuj_fragment()
                        if (len(result) == (n-5)) and (len(reqFragm) != 4):
                              break

                  result = result + reqFragm
            else:
                  result = result + losuj_fragment()

      print(result)

# wcześniej były definicje, poniżej jest część która się wykonuje

krzyzyk(5)
"""for i in range(10):
      losuj_haslo(8)
for i in range(10):
      losuj_haslo(12)
"""
"""  Zadanie pierwsze  """
"""
for i in range(10):
   print ("Przebieg:",i)
   print (20 * "-")
   if i < 5:   # parzysta
      kwadrat(3+2*i)
   else:  # czyli nieparzysta
      kwadrat2(3+i-5)
   print()    # pusty wiersz   
"""
    
"""  Zadanie Drugie  """
"""
for i in range(4,101):
      wynik = silnia(i)

      if str(len(str(wynik))).endswith('2'):
            print( i ,"! ma ",len(str(wynik))," cyfry",sep='')
      elif str(len(str(wynik))).endswith('3'):
                  print( i ,"! ma ",len(str(wynik))," cyfry",sep='')
      elif str(len(str(wynik))).endswith('4'):
            print( i ,"! ma ",len(str(wynik))," cyfry",sep='')
      else:
            print( i ,"! ma ",len(str(wynik))," cyfr",sep='')
"""
     

#"""

   
