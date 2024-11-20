from CUERPOCELESTE import CUERPOCELESTE
import math

class LUNA(CUERPOCELESTE):
    def __init__(self, PosicionX,PosicionY,  Masa,  Diametro, Nombre):
        super().__init__([PosicionX,PosicionY], Masa)
        self.Nombre = Nombre
        self.Diametro = Diametro
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
    def getDistanciaDelPlaneta(self, Planeta):
        rx = abs(Planeta.Posicion[0] - self.Posicion[0])
        ry = abs(Planeta.Posicion[1] - self.Posicion[1])
        R = math.sqrt(( (rx) * (rx) ) + ( (ry) * (ry) ) )
        return R
    def getAngulo(self):
        return self.Angulo
    def setAngulo(self,NuevoAngulo):
        self.Angulo=NuevoAngulo
