from CUERPOCELESTE import CUERPOCELESTE
import math

class PLANETA(CUERPOCELESTE):
    def __init__(self, PosicionX,PosicionY, Masa, Diametro, Atmosfera, Nombre):

        self.DistanciaAlSol = PosicionX
        super().__init__([PosicionX+500,PosicionY], Masa)
        self.Diametro = Diametro
        self.Atmosfera = Atmosfera
        self.Nombre = Nombre
        self.NumLunas = 0
        self.Angulo = 0

    def CalcularFuerzaGravitaroria(self, CuerpoAtraido):
        rx = abs(CuerpoAtraido.Posicion[0]-self.Posicion[0])
        ry = abs(CuerpoAtraido.Posicion[1] - self.Posicion[1])
        R = math.sqrt(((rx)*(rx))+((ry)*(ry)))
        G= .00000000006672
        Fuerza = (G*self.Masa*CuerpoAtraido.Masa)/(R)
        return Fuerza

    def ActualizarPosicion(self):
        self.Posicion = self.Posicion
        return self.Posicion
    def getDistanciaDelSol(self, Sol):
        rx = abs(Sol.Posicion[0] - self.Posicion[0])
        ry = abs(Sol.Posicion[1] - self.Posicion[1])
        R = math.sqrt(((rx) * (rx)) + ((ry)*(ry)))
        return R
    def AñadirLuna(self):
        self.NumLunas += 1

    def ActualizarPosicion(self):
        return self.Posicion
    def getAngulo(self):
        return self.Angulo
    def setAngulo(self,NuevoAngulo):
        self.Angulo=NuevoAngulo