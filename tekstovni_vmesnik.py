import model


def izpis_zmage(igra):
    return "ZMAGAL SI!"

#def izpis_plosce(igra):
#    presledek = "-----------------------------------"
#    print('SPOMIN')
#    igra.pokazi_plosco()
#    print(presledek)

def izpis_igre(igra):
    presledek = "-----------------------------------"
    print('SPOMIN')
    print(presledek)
    igra.pokazi()
    print(presledek)


def zahtevaj_vnos():
    p1 = input('1.karta:')
    p2 = input('2.karta:')
    izbira = p1 + p2
    return izbira

def zahtevaj_vnos2():
    return input('2.karta')
     
def pricni_igro():
    return input('klikni enter')
    

def pozeni_vmesnik():
    trenutna_igra = model.nova_igra()
    #izpis_plosce(trenutna_igra)
    #zacetek = pricni_igro()

    while True:
         
        izpis_igre(trenutna_igra)

        izbira = zahtevaj_vnos()
 
        stanje = trenutna_igra.ugibaj(izbira)

        izpis_igre(trenutna_igra)

        if trenutna_igra.zmaga():
            print(izpis_zmage(trenutna_igra))
            return
        

 

pozeni_vmesnik()

 