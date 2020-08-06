import random

VRSTICE = 4
STOLPCI = 4
VELIKOST_IGRALNE_PLOSCE = VRSTICE * STOLPCI

ZMAGA ='W'


SEZNAM_KART = ['K', 'D', 'B', '10', '9', '8', '7', 'A']

# Definirajmo logicni model igre
class Igra: 

    def __init__(self, plosca, skrita):
        self.plosca = plosca
        self.skrita = skrita


    def pokazi(self):
        # pokaze nas trenutni rezultat
        niz = ""
        for i in range(0, VRSTICE):
            for j in range(0, STOLPCI):
                niz = niz + self.skrita[i][j] + " "
            if i != VRSTICE - 1:
                niz = niz + "\n"
        print(niz)

    def ugibaj(self, izbira): 
        seznam = []
        for i in izbira:
            seznam.append(int(i))
        par_1 = [] + seznam[:2]
        ugib1 = self.plosca[par_1[0]][par_1[1]]
        par_2 = [] + seznam[2:]
        ugib2 = self.plosca[par_2[0]][par_2[1]]
        if ugib1 == ugib2:
            self.skrita[par_1[0]][par_1[1]] = ugib1
            self.skrita[par_2[0]][par_2[1]] = ugib2
        return self.skrita




    def zmaga(self):
        if self.skrita == self.plosca:
            return True
        return False



def nova_igra():
    karte = SEZNAM_KART[:(VELIKOST_IGRALNE_PLOSCE // 2)] * 2
    random.shuffle(karte)
    plosca = [karte[:4],
             karte[4:8],
             karte[8:12],
             karte[12:16]]
    skrita = [list('?' * STOLPCI) for i in range(VRSTICE)] #na zacetku igre potrebujemo prazno ploso
    return Igra(plosca, skrita)