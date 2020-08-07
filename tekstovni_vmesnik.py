import model



 

def izpis_zmage(igra):
    return "ZMAGAL SI!"





def izpis_igre(igra):
    presledek = "-----------------------------------"
    print('SPOMIN')
    igra.pokazi2()
    print(presledek)

def zahtevaj_vnos(): 
    return input('Izberi polji')
    
   
     
#def zahtevaj_tezavnost():
#    return input('1-lahko \n2-srednje \n3-tezko')
     
     


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

 