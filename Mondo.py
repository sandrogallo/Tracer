import pygraph.pycart as py
import math
import time
import random

class File():

    @staticmethod
    def takeDates(testo):
        file = open(testo, "r")
        citta = [x for x in file.readlines()]
        return citta

class Mappa:
    h_canvas = 0  # altezza dello Screen
    l_canvas = 0  # larghezza dello Screen

    def Canvas(self,high,weight):
        self.h_canvas=high
        self.l_canvas=weight
        piano = py.Plane(w=self.l_canvas, h=self.h_canvas, sx=1, axes=False,grid=False)  # creo una nuovo Screenpenna = py.Pen()  # creo un oggetto penna
        #penna = py.Pen()  # creo un oggetto penna
        #penna.drawpoint(position=(0 , 0),width=2,color="red")  # disegna l'origine

    def draw_position(self,longitudine,latitudine):
        convertitore=Conversioni()
        x = (convertitore.get_arch_x(longitudine,latitudine) * self.l_canvas / 2) / convertitore.riferimento  # proporziono i due archi in maniera tale che stiano all'interno della canvas
        y = (convertitore.get_arch_y(latitudine) * self.h_canvas / 2) / convertitore.cir_minore
        print(x)
        print(y)
        penna = py.Pen()  # creo un oggetto penna
        penna.drawpoint(position=(x, y), width=2)  # disegno il punto con le specifiche cordinate

class Conversioni():

    riferimento = 20000  # lunghezza di un meridiano(km)
    cir_terra = 40000  # lunghezza della circonferenza(km)
    raggio_terra = 6370  # raggio della terra(km)
    cir_minore=0

    def __get_radian(self,degree):
        radian = (degree * 3.14) / 180  # converto la longitudine in radianti
        return radian

    def get_arch_y(self,angle):
        # converte la latitudine in un arcocon formula arco=(Cterra*latitudine)/360
        arco_y = (self.cir_terra * angle) / 360
        return arco_y

    def get_arch_x(self,angle,latitudine):
        # la latitudine si misura su circonferenze minori a quella dell'equatore
        # quindi la formula per ricavare la circonferenza minore è C=2*(raggio_terra*(coseno longitudine))*pigreco
        if  latitudine>90:
            latitudine+=270
        elif latitudine<0:
            latitudine=-latitudine+90

        print(latitudine)
        self.cir_minore = 2 * (self.raggio_terra * math.cos(self.__get_radian(latitudine))) * 3.14
        arco_x = (angle * self.cir_minore) / 360  # ricavo la lunghezza dell'arco analogamente all'arco della latitudine
        return arco_x

    def change_riferimento(self,lista):
        pass

mondo=Mappa()
mondo.Canvas(500,600)
lista=[]
for x in range(10):#disegna 10 punti random e stampa le cordinate
    x1,y=random.randint(-90,90),random.randint(-180,180)
    print(x1)
    print(y)
    lista.append(x1)
    lista.append(y)

mondo.draw_position(68,98)

time.sleep(20)
