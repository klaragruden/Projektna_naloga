import model


def izpis_zmage(igra):
    return "ZMAGAL SI!"



def izpis_igre(igra):
    presledek = "-----------------------------------"
    print('SPOMIN')
    print(presledek)
    igra.pokazi()
    print(presledek)


def zahtevaj_vnos():
    return input('izberi polja')
     

    
    
         


def pozeni_vmesnik():
    # nova igra
    trenutna_igra = model.nova_igra()

    while True:
        #pokazemo stanje
         
        izpis_igre(trenutna_igra)

        izbira = zahtevaj_vnos()
 

        rezultat = trenutna_igra.ugibaj(izbira)

        izpis_igre(trenutna_igra)

        if trenutna_igra.zmaga():
            print(izpis_zmage(trenutna_igra))
            return
        

 

pozeni_vmesnik()

 