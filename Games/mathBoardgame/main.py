import pygame, sys, random, os, math
import numpy as np
from pytam import *
import stany
import wyswietlanie
#from textwrap import fill

pygame.init()

#/////////Zmienne///////////

gameState = stany.stanGry()

"""
0-otwarcie
1-ruchy
2-zadanie
"""

wsp_pytan = [2,3,5,8,10,14,16,18,23,25,28,30,34,35,40,42,45,49,51,54,55,57,59]
wsp_historyjki1 = [4,9,20,32,43,56]
wsp_historyjki2=[1,6,12,26,37,47]




#TODO fix
#pytania=[" Oblicz: ∫x² dx","Liczba √2 jest równa:", "Liczba √a*n√a  jest równa:"] # pytania awaryjnie
pytania=wybor_pytania() #przesyłam pytania
#pytania = open("pytania.txt").readlines() # chwilowo nie działa
historyjki1= open("Historyjki1.txt").readlines()
historyjki2=open("Historyjki2.txt").readlines()

#####/////Obrazki//////////

Historyjka = pygame.image.load("historyjka.jpg")


#//////////PYGame initialization////////////
pygame.init()
 #pozycja kwadratu w którym zmieniam x współrzędną czyli przesuwam w prawo
pygame.display.set_caption('MATHwar') #napis


draw = wyswietlanie.wyswietl(gameState)


#/////////Funkcje////////
def wybor():
    kostka = random.randrange(1,6)
    return (kostka)


"""Artefact
def blit_text(surface, text, pos, font, color=pygame.Color('black')): # funkcja, do "łamania" tekstu, średnio działa
    SIZE = WIDTH, HEIGHT = (210, 180)
    FPS = 30
    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.
"""


#/////////MAIN///////////

while True: 
    draw.w_plansze

    #TODO event handler class
    for event in pygame.event.get():
        stanGry = gameState.getStan
        pozycja = gameState.getPozycja
        ectsy = gameState.getECTSY
        if event.type == pygame.QUIT: #akcja zamknięcia programu
            sys.exit(0)
        if event.type == pygame.KEYDOWN:
            if stanGry == 0:
                if event.key == pygame.K_f: #wywołuje przyciskiem f 
                    rzut=wybor()
                    ### zakręty na planszy
                    temp=15-pozycja%15 # tyle brakuje do zakrętu
                    if rzut < temp: # sprawdzamy czy wyrzuciliśmy na kostce mniej oczek niż jest do zakrętu
                        draw.przesunPionek(rzut) # zmiana pozycji kwadratu
                        pozycja+=rzut
                        pozycja=pozycja%60
                    else: 
                        draw.przesunPionek(temp) # przesunięcie pionka "do zakrętu"
                        pozycja+=rzut
                        pozycja=pozycja%60
                        draw.przesunPionek(rzut-temp) # dalsze przesunięcie pionka
                    draw.w_kostke(rzut) # wyświetla rzut na kostce
                    
                    # chcemy wyświetlać okienko z pytaniem tylko po rzucie kostką 
                    # (wcześniejszy błąd: okno wyświetlało się bezpośrednio po udzieleniu odpowiedzi)
                    if pozycja in wsp_pytan:    #wyświetlanie okienka z pytaniem
                        #TODO fix baza danych bs
                        stanGry = 1
                        text1=random.choice(pytania) #losuje pytanie
                        #hist1=random.choice(historyjki1) # losuje historyjki
                        #hist2=random.choice(historyjki2)
                        numer=numer_pytania(text1) #sprawdzam numer pytania
                        gameState.pytanie = [
                            [odp_a(numer),320,370], #dopasowuje odpowiedź a do konkretnego pytania
                            [odp_b(numer),320,410], #dopasowuje odpowiedź b do konkretnego pytania
                            [odp_c(numer),530,370], #dopasowuje odpowiedź c do konkretnego pytania
                            [odp_d(numer),530,410] #dopasowuje odpowiedź d do konkretnego pytania
                        ]
                        gameState.pop_odp=poprawne(numer) #sprawdza która odp jest poprawna
                    if pozycja in wsp_historyjki1:
                        hist1=random.choice(historyjki1)
                        stanGry = 2
                    if pozycja in wsp_historyjki2:
                        hist2=random.choice(historyjki2)
                        stanGry = 3
            if stanGry == 2 or 3:
                if event.key == pygame.K_o: #wyłączamy historyjkę
                    stanGry = 0
                

            if stanGry == 1:
                if event.key == pygame.K_o:
                    gameState.userInput = 0
                #TODO classa odczytujaca poprawne odpowiedzi z bazy pytań
                if event.key == pygame.K_a and "a" == gameState.pop_odp or event.key == pygame.K_b and "b" == gameState.pop_odp  or event.key == pygame.K_c and "c" == gameState.pop_odp or event.key == pygame.K_d and "d" == gameState.pop_odp:
                #wywołuje przyciskiem a
                
                        #screen.blit(poprawna_odp,(220,200)) # wyswietla info że odp poprawna
                    gameState.userInput = 1
                else:
                        #screen.blit(zla_odp,(220,200))# wyswietla info że odp zla
                    gameState.userInput = -1

                if gameState.userInput != 0: # != różne #jeżeli odp. została udzielona
                    ectsy += gameState.userInput # dodaj/odejmij punkty
                    stanGry = 0
        gameState.setStan(stanGry)
        gameState.setPozycja(pozycja)
        gameState.setECTSY(ectsy)

    if stanGry == 0: 
        pass
        

    if stanGry == 1:

        draw.w_okienko(2) # wyswietla okienko 
        draw.w_text(text1,270,250)

        #TODO wyswietl texty odpowiedzi za pomoca clasy odpowiedzi
        for item in gameState.pytanie:
           draw.w_text(item[0],item[1],item[2])
        #TODO timer for question feedback
        if gameState.userInput == 1:
            draw.w_okienko(0)
        elif gameState.userInput == -1:
            draw.w_okienko(1)

    #TODO stan gry dla kart szansy
    if stanGry == 2:
        draw.w_obrazek(Historyjka,220,200)
        draw.w_text(hist1,270,250)

    
    """
    if stanGry == 3:
        screen.blit(Historyjka, (220,200)) # wyswietla historyjkę2
        hist2_render=czcionka.render(hist2,1,(0, 0, 0)) #tekst
        screen.blit(hist2_render,(270,250)) #wyswietla tekst
        blit_text(Historyjka, hist2,(20,20),czcionka,)
            #if event.key == pygame.K_o: #wyłączamy historyjkę
             #   stanGry = 0
    """
    draw.draw


    