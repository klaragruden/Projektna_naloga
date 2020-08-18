import random
import json

VRSTICE = 4
STOLPCI1 = 4
STOLPCI2 = 6
 
ZACETEK = 'S'

#ZMAGA ='W'

TEZAVNOST_LAHKO = 1
TEZAVNOST_SREDNJE = 2
TEZAVNOST_TEZKO = 3

SEZNAM_KART1 = ['K', 'D', 'B', '10', '9', '8', '7', 'A']
SEZNAM_KART2 = ['K', 'D', 'B', '10', '9', '8', '7', 'A', '6', '5', '4', '3']

DATOTEKA_STANJE = 'stanje.json'

# Definirajmo logicni model igre
class Igra: 

    def __init__(self, plosca, skrita, tezavnost):
        self.plosca = plosca
        self.skrita = skrita
        self.tezavnost = tezavnost
   

    def pokazi(self):
        # pokaze nas trenutni rezultat
        if self.tezavnost == TEZAVNOST_LAHKO:
            niz = ""
            for i in range(0, VRSTICE):
                for j in range(0, STOLPCI1):
                    niz = niz + self.skrita[i][j] + " "
                if i != VRSTICE - 1:
                    niz = niz + "\n"
            print(niz)
        elif self.tezavnost == TEZAVNOST_SREDNJE:
            niz = ""
            for i in range(0, VRSTICE):
                for j in range(0, STOLPCI2):
                    niz = niz + self.skrita[i][j] + " "
                if i != VRSTICE - 1:
                    niz = niz + "\n"
            print(niz)
        elif self.tezavnost == TEZAVNOST_TEZKO:
            niz = ""
            for i in range(0, VRSTICE):
                for j in range(0, STOLPCI2):
                    niz = niz + self.skrita[i][j] + " "
                if i != VRSTICE - 1:
                    niz = niz + "\n"
            print(niz)
        else:
            print('vnesite veljavno tezavnost (1, 2 ali 3) ')

   

    def ugibaj(self, izbira):
        seznam = []
        if self.tezavnost == TEZAVNOST_TEZKO:
            for i in izbira:
                seznam.append(int(i))
            par_1 = [] + seznam[:2]
            ugib1 = self.plosca[par_1[0]][par_1[1]]
            par_2 = [] + seznam[2:4]
            ugib2 = self.plosca[par_2[0]][par_2[1]]
            par_3 = [] + seznam[4:]
            ugib3 = self.plosca[par_3[0]][par_3[1]]
            if par_1 == par_2 == par_3 or par_3 == par_2 or par_3 == par_1 or par_1 == par_2:
                return self.plosca
            if ugib1 == ugib2 == ugib3:
                self.skrita[par_1[0]][par_1[1]] = ugib1
                self.skrita[par_2[0]][par_2[1]] = ugib2
                self.skrita[par_3[0]][par_2[1]] = ugib3
            return self.skrita    
        elif self.tezavnost == TEZAVNOST_SREDNJE:
            for i in izbira:
                seznam.append(int(i))
            par_1 = [] + seznam[:2]
            ugib1 = self.plosca[par_1[0]][par_1[1]]
            par_2 = [] + seznam[2:]
            ugib2 = self.plosca[par_2[0]][par_2[1]]
            if par_1 == par_2:
                return self.plosca
            if ugib1 == ugib2:
                self.skrita[par_1[0]][par_1[1]] = ugib1
                self.skrita[par_2[0]][par_2[1]] = ugib2
            return self.skrita  
        elif self.tezavnost == TEZAVNOST_LAHKO:
            for i in izbira:
                seznam.append(int(i))
            par_1 = [] + seznam[:2]
            ugib1 = self.plosca[par_1[0]][par_1[1]]
            par_2 = [] + seznam[2:]
            ugib2 = self.plosca[par_2[0]][par_2[1]]
            if par_1 == par_2:
                return self.plosca
            if ugib1 == ugib2:
                self.skrita[par_1[0]][par_1[1]] = ugib1
                self.skrita[par_2[0]][par_2[1]] = ugib2
            return self.skrita
        else:
            print('vneseni veljavno tezavnost (1, 2 ali 2)')
    
     

    def zmaga(self):
        if self.skrita == self.plosca:
            return True
        return False


def nova_igra():
    tezavnost = int(input(""" "Izberi tezavnost (lahko = 1, srednje = 2, tezko = 3): """))
    if tezavnost == TEZAVNOST_LAHKO:
        return nova_igra_lahko()
    elif tezavnost == TEZAVNOST_SREDNJE:
        return nova_igra_srednje()
    elif tezavnost == TEZAVNOST_TEZKO:
        return nova_igra_tezko()
    else:
        print('izberi veljavno tezavnost (1, 2 ali 3)')


def nova_igra_lahko():
    karte = SEZNAM_KART1[:(VRSTICE * STOLPCI1 // 2)] * 2
    random.shuffle(karte)
    tezavnost = TEZAVNOST_LAHKO
    plosca = [karte[:4],
             karte[4:8],
             karte[8:12],
             karte[12:16]]
    skrita = [list('?' * STOLPCI1) for i in range(VRSTICE)] #na zacetku igre potrebujemo prazno ploso
    return Igra(plosca, skrita, tezavnost)


def nova_igra_srednje():
    karte = SEZNAM_KART2[:(VRSTICE * STOLPCI2 // 2)] * 2
    random.shuffle(karte)
    tezavnost = TEZAVNOST_SREDNJE
    plosca = [karte[:6],
             karte[6:12],
             karte[12:18],
             karte[18:24]]
    skrita = [list('?' * STOLPCI2) for i in range(VRSTICE)] #na zacetku igre potrebujemo prazno ploso
    return Igra(plosca, skrita, tezavnost)

 
def nova_igra_tezko():
    karte = SEZNAM_KART2[:(VRSTICE * STOLPCI2 // 3)] * 3
    random.shuffle(karte)
    tezavnost = TEZAVNOST_TEZKO
    plosca = [karte[:6],
             karte[6:12],
             karte[12:18],
             karte[18:24]]
    skrita = [list('?' * STOLPCI2) for i in range(VRSTICE)] #na zacetku igre potrebujemo prazno ploso
    return Igra(plosca, skrita, tezavnost)


class Spomin:

    def __init__(self, datoteka_s_stanjem):
        self.datoteka_s_stanjem = datoteka_s_stanjem
        self.nalozi_igre_iz_datoteke()
         

    def prost_id_igre(self):
        if len(self.igre) == 0:
            return 0
        else:
            return max(self.igre.keys()) + 1

    def nova_igra(self):
        id_igre = self.prost_id_igre()
        igra = nova_igra()
        self.igre[id_igre] = (igra, ZACETEK)
        self.zapisi_igre_v_datoteko()
        return id_igre

    def ugibaj(self, id_igre, karta):
        igra, _ = self.igre[id_igre]
        stanje = igra.ugibaj(karta)
        self.igre[id_igre] = (igra, stanje)
        self.zapisi_igre_v_datoteko()

    def nalozi_igre_iz_datoteke(self): 
        with open(self.datoteka_s_stanjem, 'r', encoding='utf-8') as f: 
            igre = json.load(f)
            self.igre = {int(id_igre): (Igra(plosca, skrita, tezavnost), stanje) for id_igre, (plosca, skrita, tezavnost, stanje) in igre.items()}

    def zapisi_igre_v_datoteko(self): 
        with open(self.datoteka_s_stanjem, 'w', encoding='utf-8') as f: 
            igre = {id_igre: (igra.plosca, igra.skrita, igra.tezavnost, stanje) for id_igre, (igra, stanje) in self.igre.items()}
            json.dump(igre, f)



