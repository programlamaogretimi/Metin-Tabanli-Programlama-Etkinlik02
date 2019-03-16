import turtle

def dogu():
    turtle.seth(0)

def kuzey():
    turtle.seth(90)

def bati():
    turtle.seth(180)

def guney():
    turtle.seth(270)

def catiSag(adim):
    turtle.seth(120)
    turtle.fd(adim)

def catiSol(adim):
    turtle.seth(240)
    turtle.fd(adim)

def ucgenSag(adim):
    turtle.seth(120)
    turtle.fd(adim)
    turtle.seth(270)

def ucgenSol(adim):
    turtle.seth(240)
    turtle.fd(adim)
    turtle.seth(270)

def solaDon():
    turtle.lt(90)

def sagaDon():
    turtle.rt(90)

def ciz(adim):
    turtle.fd(adim)

def git(adim):
    turtle.pu()
    turtle.fd(adim)
    turtle.pd()
    
def kalemAcik():
    turtle.pd()

def kalemKapali():
    turtle.pu()

def cokgenCiz(uzunluk, kenar):
    for i in range(kenar):
        turtle.fd(uzunluk)
        turtle.lt(360/kenar)
    
    
