class stanGry():
    pozycja = None
    stan = None
    ectsy = None
    userInput = None
    pytanie = None
    pop_odp = None

    def __init__(self):
        self.pozycja = 0
        self.stan = 0
        self.ectsy = 0
        self.userInput = 0

    def getPozycja(self):
        return self.pozycja
    def setPozycja(self, pozycja):
        self.pozycja = pozycja

    def getStan(self):
        return self.stan
    def setStan(self, stan):
        self.stan = stan

    def getECTSY(self):
        return self.ectsy
    def setECTSY(self, ectsy):
        self.ectsy = ectsy