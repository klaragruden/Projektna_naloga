import bottle
import model
#from bottle import request
	
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
     

@bottle.get("/igra/")
def pokazi_igro():
    id_igre = int(bottle.request.get_cookie(PISKOTEK, secret=SKRIVNOST))
    igra, stanje = spomin.igre[id_igre]
    if spomin.tezavnost == 1:
        tpl = "views/igra1.tpl"
    if spomin.tezavnost == 2:
        tpl = "views/igra2.tpl"
    if spomin.tezavnost == 3:
        tpl = "views/igra3.tpl"
    return bottle.template(tpl, igra=igra, stanje=stanje)



@bottle.post('/igra/')
def ugibaj(): 
    id_igre = int(bottle.request.get_cookie(PISKOTEK, secret=SKRIVNOST))
    if spomin.tezavnost == 1:
        izbira1 = bottle.request.forms.getunicode('izbira1')
        izbira2 = bottle.request.forms.getunicode('izbira2')
        izbira = izbira1 + izbira2
    if spomin.tezavnost == 2:
        izbira1 = bottle.request.forms.getunicode('izbira1')
        izbira2 = bottle.request.forms.getunicode('izbira2')
        izbira = izbira1 + izbira2
    if spomin.tezavnost == 3:
        izbira1 = bottle.request.forms.getunicode('izbira1')
        izbira2 = bottle.request.forms.getunicode('izbira2') 
        izbira3 = bottle.request.forms.getunicode('izbira3')
        izbira = izbira1 + izbira2 + izbira3
    spomin.ugibaj(id_igre, izbira)
    bottle.redirect('/igra/')

 
bottle.run(debug=True, reloader=True)







