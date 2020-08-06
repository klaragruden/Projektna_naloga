import model



def izpis_poraza(igra):
    return "IZGUBIL SI, več sreče prihodnjič!"

def izpis_zmage(igra):
    return "ZMAGAL SI!"

def izpis_remija(igra):
    return "NEODLOČENO, poskusi še enkrat!"

def izpis_igre(igra):
    presledek = "-----------------------------------"
    igra.pokazi()
    print(presledek)

def zahtevaj_vnos():
    return input("Izberi:")

def pozeni_vmesnik():
    # nova igra
    trenutna_igra = model.nova_igra()

    while True:
        #pokazemo stanje
        izpis_igre(trenutna_igra)

        izbira = zahtevaj_vnos()
 

        rezultat = trenutna_igra.ugibaj(izbira)

        izpis_igre(trenutna_igra)

 

pozeni_vmesnik()

 