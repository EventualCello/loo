from CUERPOCELESTE import CUERPOCELESTE
import math


class ESTRELLA(CUERPOCELESTE):
    def __init__(self):
        super().__init__([200,200], 500, 1000)
        self.Luminocidad = 400
        self.Temperatura = 4000

    def CalcularFuerzaGravitaroria(self, CuerpoAtraido):
        rx = abs(CuerpoAtraido.Posicion[0]-self.Posicion[0])
        ry = abs(CuerpoAtraido.Posicion[1] - self.Posicion[1])
        R = math.sqrt(((rx)*(rx))+((ry)(ry)))
        G= .00000000006672
        Fuerza = (G*self.Masa*CuerpoAtraido.Masa)/(R)
        return Fuerza

    def ActualizarPosicion(self):
        return self.Posicion
