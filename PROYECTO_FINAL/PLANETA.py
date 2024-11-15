from CUERPOCELESTE import CUERPOCELESTE
import math

class PLANETA(CUERPOCELESTE):
    def __init__(self, Posicion, VelocidadRot, Masa, Diametro, Atmosfera, NumLunas):
        super().__init__(Posicion, VelocidadRot, Masa)
        self.Diametro = Diametro
        self.Atmosfera = Atmosfera
        self.NumLunas = NumLunas

    def CalcularFuerzaGravitaroria(self, CuerpoAtraido):
        rx = abs(CuerpoAtraido.Posicion[0]-self.Posicion[0])
        ry = abs(CuerpoAtraido.Posicion[1] - self.Posicion[1])
        R = math.sqrt(((rx)*(rx))+((ry)(ry)))
        G= .00000000006672
        Fuerza = (G*self.Masa*CuerpoAtraido.Masa)/(R)
        return Fuerza

    def ActualizarPosicion(self):
        self.Posicion = self.Posicion
        return self.Posicion

    def AñadirLuna(self):
        self.NumLunas += 1