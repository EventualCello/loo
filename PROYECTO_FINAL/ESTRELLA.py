from CUERPOCELESTE import CUERPOCELESTE
import math


class ESTRELLA(CUERPOCELESTE):
    def __init__(self):
        super().__init__([500,350], 1000)
        self.Luminocidad = 400
        self.Temperatura = 4000
        self.Angulo = 0

    def CalcularFuerzaGravitaroria(self, CuerpoAtraido):
        rx = abs(CuerpoAtraido.Posicion[0]-self.Posicion[0])
        ry = abs(CuerpoAtraido.Posicion[1] - self.Posicion[1])
        R = math.sqrt(((rx)*(rx))+((ry)*(ry)))
        G= .00000000006672
        Fuerza = (G*self.Masa*CuerpoAtraido.Masa)/(R)
        return Fuerza

    def ActualizarPosicion(self):
        return self.Posicion
    def getPosicionX(self):
        return self.Posicion[0]
    def getPosicionY(self):
        return self.Posicion[1]
    '''def getRadio(self):
        return self.Radio'''
    def getAngulo(self):
        return self.Angulo
    def setAngulo(self,NuevoAngulo):
        self.Angulo=NuevoAngulo
