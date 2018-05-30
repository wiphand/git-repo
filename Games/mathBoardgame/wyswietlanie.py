import pygame
import stany
class wyswietl():

    screen = pygame.display.set_mode((1280, 720))
    czcionka=pygame.font.SysFont("comicsansms",20)
    czcionka1=pygame.font.SysFont("comicsansms",30)

    okienka = [
        pygame.image.load("poprawna.png"),
        pygame.image.load("zla.png"),
        pygame.image.load("pytanie1.jpg")
    ]
    

    Pionek= pygame.image.load("Pi.png")
    wspolrzednePionka=pygame.Rect(176,58,20,20)

    plansza = pygame.image.load("plansza1.jpg")

    kostki = None
    stan = None


    def __init__(self,stan: "stanGry"):
        self.stan = stan
        self.kostki =  [pygame.image.load("1.png"),
                        pygame.image.load("2.png"),
                        pygame.image.load("3.png"),
                        pygame.image.load("4.png"),
                        pygame.image.load("5.png"),
                        pygame.image.load("6.png")]
    def w_plansze(self):
        self.screen.blit(self.plansza, [0, 0])

    def w_okienko(self,typ):
        self.screen.blit(self.okienka[typ],(220,200))

    def w_kostke(self,x):
        self.screen.blit(self.kostki[x-1], (1100,600))

    def w_text(self,text,x,y):
        render=self.czcionka.render(text,1,(0, 0, 0)) 
        self.screen.blit(render,(x,y)) #wyswietla odp a

    def w_obrazek(self,obrazek,x,y):
        self.screen.blit(obrazek, (x,y))

    def przesunPionek(self,rzut):
        if self.stan.getPozycja() < 15:
            self.wspolrzednePionka.x +=41*rzut
        elif self.stan.getPozycja() < 30:
            self.wspolrzednePionka.y +=41*rzut
        elif self.stan.getPozycja() < 45:
            self.wspolrzednePionka.x -=41*rzut
        elif self.stan.getPozycja() < 60:
            self.wspolrzednePionka.y -=41*rzut

    def draw(self):
        text_render = self.czcionka1.render(str(self.stan.getECTSY), 1, (0, 0, 0))
        self.screen.blit(text_render,(90,30)) # ECTS
        self.screen.blit(self.Pionek, self.wspolrzednePionka) # pionek

        #///////////////////////
        pygame.display.update()
        pygame.display.flip()