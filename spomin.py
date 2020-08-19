import bottle
import model
from bottle import request
	
SKRIVNOST = 'moja skrivnost'
PISKOTEK = 'idigre'
 

spomin = model.Spomin(model.DATOTEKA_STANJE)
 

@bottle.get('/')
def index():
    return bottle.template('views/index.tpl')


@bottle.post('/nova_igra/')
def nova_igra():
    tezavnost = int(bottle.request.forms['tezavnost'])
    id_igre = spomin.nova_igra(tezavnost)
    bottle.response.set_cookie(PISKOTEK, str(id_igre), path='/', secret=SKRIVNOST)
    #bottle.redirect('/igra/?tezavnost=' + str(tezavnost) + '&id_igre=' + str(id_igre) + '&kliknjena=')
    bottle.redirect('/plosca/')

@bottle.get('/plosca/')
def pokazi_plosco():
    id_igre = int(bottle.request.get_cookie(PISKOTEK, secret=SKRIVNOST))
    igra, stanje = spomin.igre[id_igre]
    if spomin.tezavnost == 1:
        tpl = "views/igra_zacetek.tpl"
    if spomin.tezavnost == 2:
        tpl = "views/igra1_zacetek.tpl"
    if spomin.tezavnost == 3:
        tpl = "views/igra1_zacetek.tpl"
    return bottle.template(tpl, igra=igra, stanje=stanje)

@bottle.post('/pricni_igro/')
def nova_igra():
    tezavnost = int(bottle.request.get_cookie(PISKOTEK, secret=SKRIVNOST))
    id_igre = int(bottle.request.get_cookie(PISKOTEK, secret=SKRIVNOST))
    bottle.response.set_cookie(PISKOTEK, str(id_igre), path='/', secret=SKRIVNOST)
    bottle.redirect('/igra/')
    #bottle.redirect('/igra/?tezavnost=' + str(tezavnost) + '&id_igre=' + str(id_igre) + '&kliknjena=')

@bottle.get("/igra/")
def pokazi_igro():
    id_igre = int(bottle.request.get_cookie(PISKOTEK, secret=SKRIVNOST))
    igra, stanje = spomin.igre[id_igre]
    if spomin.tezavnost == 1:
        tpl = "views/igra.tpl"
    if spomin.tezavnost == 2:
        tpl = "views/igra1.tpl"
    if spomin.tezavnost == 3:
        tpl = "views/igra1.tpl"
    return bottle.template(tpl, igra=igra, stanje=stanje)



@bottle.post('/igra/')
def ugibaj(): 
    id_igre = int(bottle.request.get_cookie(PISKOTEK, secret=SKRIVNOST))
    izbira = bottle.request.forms.getunicode('izbira')
    spomin.ugibaj(id_igre, izbira)
    bottle.redirect('/igra/')

 
bottle.run(debug=True, reloader=True)







