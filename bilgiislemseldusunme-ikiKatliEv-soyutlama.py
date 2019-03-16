from etkinlik import *

def katCiz(katSayisi):
    for i in range(katSayisi):
        for j in range(4):
        #kare çizimi
            ciz(50) #50 birim kenar çiz
            solaDon() #sol yöne dön
        #bir sonraki katın çizilmeye başlanacağı
        #noktaya git
        solaDon()#kuzey yönüne dön
        git(50)  #Karenin sol üst köşesine git
        sagaDon()#Üçgen çizimine başlamak için
                     #doğu yönüne dön
def catiCiz():
    #üçgen çizimi
    ciz(50)      #50 birim üçgen
                 #tabanını çiz
    ucgenSag(50) #50 birim üçgen
                 #sağ kenarını çiz
    ucgenSol(50) #50 birim üçgen
                 #sol kenarını çiz

katCiz(2)
catiCiz()

#solaDon()
#git(1*50)






































#dogu()
#git(50)
#kuzey()
#git(50)


#ciz(50)
#bati()
#ciz(50)
#guney()
#ciz(50)


#catiSag(50)
#git(50)
#turtle.seth(240)
#turtle.fd(50)
#catiSol(50)

