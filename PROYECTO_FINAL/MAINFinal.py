from CUERPOCELESTE import CUERPOCELESTE
from ESTRELLA import ESTRELLA
from LUNA import LUNA
from PLANETA import PLANETA
import math
from tkinter import *
from tkinter import messagebox

Sol = ESTRELLA()
class Proyecto:
    def __init__(self, root):
        self.root = root
        root.title('Cuerpos Celestes')
        root.geometry('1000x700+275+25')

        self.planetas=[]
        self.CantidadPlanetas=0
        self.espacio = Canvas(root, bg='black')
        self.espacio.pack(fill=BOTH, expand=True)

        self.btnPlaneta = Button(root, text='Crear Planeta', command=self.CrearPlaneta)
        self.btnPlaneta.pack(side=LEFT)

        self.btnLuna = Button(root, text='Crear Luna', command=self.CrearLuna)
        self.btnLuna.pack(side=LEFT)

        self.btnPausa = Button(root, text='Pausar', command=self.Pausar)
        self.btnPausa.pack(side=LEFT)

        self.btnAjustarVelocidadMas = Button(root, text='Mas Velocidad', command=self.AjustarVelocidadMas)
        self.btnAjustarVelocidadMas.pack(side=LEFT)
        self.btnAjustarVelocidadMenos = Button(root, text='Menos Velocidad', command=self.AjustarVelocidadMenos)
        self.btnAjustarVelocidadMenos.pack(side=LEFT)

        self.btnSalir = Button(root, text='Salir', command=root.quit)
        self.btnSalir.pack(side=LEFT)

        self.HacerSol()
        self.VelocidadPlaneta = 2
        self.VelocidadLuna = self.VelocidadPlaneta*2
        self.MoverEspacio()

    def HacerSol(self):
        self.espacio.create_oval(Sol.getPosicionX() - 30, Sol.getPosicionY()- 30,Sol.getPosicionX() + 30, Sol.getPosicionY()+ 30,fill='yellow')
    def CrearPlaneta(self):
        CPlaneta = Toplevel(self.root)
        CPlaneta.title("Crea tu Planeta")
        CPlaneta.geometry('300x140+500+250')

        Label(CPlaneta, text="Nombre del Planeta:").grid(row=0, column=0)
        nombreEntry = Entry(CPlaneta)
        nombreEntry.grid(row=0, column=1)

        Label(CPlaneta, text="Masa del Planeta:").grid(row=1, column=0)
        masaEntry = Entry(CPlaneta)
        masaEntry.grid(row=1, column=1)

        Label(CPlaneta, text="Distancia desde el Sol (Sobre eje X):").grid(row=2, column=0)
        distanciaEntry = Entry(CPlaneta)
        distanciaEntry.grid(row=2, column=1)

        Label(CPlaneta, text="Diametro del Planeta:").grid(row=3, column=0)
        diametroEntry = Entry(CPlaneta)
        diametroEntry.grid(row=3, column=1)

        Label(CPlaneta, text="Atmosfera del Planeta:").grid(row=4, column=0)
        atmosferaEntry = Entry(CPlaneta)
        atmosferaEntry.grid(row=4, column=1)

        btnGuardar = Button(CPlaneta, text="Guardar",
                             command=lambda: [self.GuardarPlaneta(nombreEntry.get(), masaEntry.get(),
                                                                distanciaEntry.get(), diametroEntry.get(),
                                                                atmosferaEntry.get()), CPlaneta.destroy()])
        btnGuardar.grid(row=5, columnspan=2)
        return 0
    def GuardarPlaneta(self, nombre, masa, distancia, diametro, atmosfera):
        try:
            masa = float(masa)
            distancia = float(distancia)
            diametro = float(diametro)
            atmosfera = float(atmosfera)
            if masa <= 0 or distancia <= 0 or diametro <= 0 or atmosfera <= 0:
                raise ValueError("Solo el nombre puede no se un numero")

            # Agrega el planeta a la lista de planetas
            InstanciaPlaneta = PLANETA(distancia,350, masa, diametro, atmosfera, nombre)

            self.planetas.append(InstanciaPlaneta)
            self.CantidadPlanetas+=1
            messagebox.showinfo("Genial", f"Planeta '{nombre}' creado. Es el numero:{self.CantidadPlanetas} ")

        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def CrearLuna(self):
        CLuna = Toplevel(self.root)
        CLuna.title("Crea tu Luna")
        CLuna.geometry('300x140+500+250')

        Label(CLuna, text="Nombre de la Luna:").grid(row=0, column=0)
        nombreEntry = Entry(CLuna)
        nombreEntry.grid(row=0, column=1)

        Label(CLuna, text="Masa de la Luna:").grid(row=1, column=0)
        masaEntry = Entry(CLuna)
        masaEntry.grid(row=1, column=1)

        Label(CLuna, text="Distancia desde el planeta (Sobre eje X):").grid(row=2, column=0)
        distanciaEntry = Entry(CLuna)
        distanciaEntry.grid(row=2, column=1)

        Label(CLuna, text="Diametro de la Luna:").grid(row=3, column=0)
        diametroEntry = Entry(CLuna)
        diametroEntry.grid(row=3, column=1)

        Label(CLuna, text="Planeta Asignado (Su número de creación):").grid(row=4, column=0)
        planetaEntry = Entry(CLuna)
        planetaEntry.grid(row=4, column=1)

        btnGuardar = Button(CLuna, text="Guardar",
                            command=lambda: [self.GuardarLuna(nombreEntry.get(), masaEntry.get(),
                                                                 distanciaEntry.get(), diametroEntry.get(),
                                                                 planetaEntry.get()), CLuna.destroy()])
        btnGuardar.grid(row=5, columnspan=2)
        return 0
    def GuardarLuna(self, nombre, masa, distancia, diametro, planeta):
        try:
            masa = float(masa)
            distancia = float(distancia)
            diametro = float(diametro)
            planeta = int(planeta)-1
            if masa <= 0 or distancia <= 0 or diametro <= 0:
                raise ValueError("Solo el nombre puede no se un numero")

            # Agrega el planeta a la lista de planetas
            self.planetas[planeta].AñadirLuna(distancia+self.planetas[planeta].Posicion[0],350,  masa, diametro, nombre)

            messagebox.showinfo("Genial", f"Luna '{nombre}' creada.")

        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def Pausar(self):
        Vel = self.VelocidadPlaneta
        self.VelocidadPlaneta = 0
        self.VelocidadLuna = 0
        messagebox.showinfo("Pausa", "El juego está pausado. Aceptar para retornar")
        self.VelocidadPlaneta = Vel
        self.VelocidadLuna = Vel*2
    def AjustarVelocidadMas(self):
        self.VelocidadPlaneta += 2
        self.VelocidadLuna = self.VelocidadPlaneta * 2
    def AjustarVelocidadMenos(self):
        if self.VelocidadPlaneta >= 3:
            self.VelocidadPlaneta -= 2
            self.VelocidadLuna = self.VelocidadPlaneta * 2
        elif self.VelocidadPlaneta <= 2:
            messagebox.showinfo("Error", "La velocidad no puede bajar más")
    def MoverEspacio(self):
        self.espacio.delete("planetas")  # Limpia los planetas anteriores

        for planeta in self.planetas:
            # CÁLCULO DE TRIGONOMETRÍA PARA CHECAR LA POSICIÓN
            xPlaneta = Sol.getPosicionX() + planeta.DistanciaAlSol * math.cos(math.radians(planeta.getAngulo()))
            yPlaneta = Sol.getPosicionY() + planeta.DistanciaAlSol * math.sin(math.radians(planeta.getAngulo()))

            # HACER EL PLANETA
            radio = planeta.Diametro/2  # Radio del planeta
            self.espacio.create_oval(xPlaneta - radio, yPlaneta - radio, xPlaneta + radio, yPlaneta + radio, fill='green', tags="planetas")

            # CON EL ÁNGULO SIMULAMOS LA ROTACIÓN
            planeta.setAngulo(planeta.getAngulo() + self.VelocidadPlaneta)

            # MANTENER EL ÁNGULO MENOR A 360 PARA NO ROMPER EL CÓDIGO
            if planeta.getAngulo() >= 360:
                planeta.setAngulo(planeta.getAngulo() - 360)

            for luna in planeta.Lunas:
                # LO MISMO DE LA TRINOMETRÍA PARA LA LUNA
                xLuna = xPlaneta + luna.getDistanciaDelPlaneta(planeta) * math.cos(math.radians(luna.getAngulo()))
                yLuna = yPlaneta + luna.getDistanciaDelPlaneta(planeta) * math.sin(math.radians(luna.getAngulo()))

                # PLASMAR LA LUNA
                radioL = luna.Diametro / 2  # Radio del planeta
                self.espacio.create_oval(xLuna - radioL, yLuna - radioL, xLuna + radioL, yLuna + radioL, fill='grey', tags="planetas")

                # Actualiza el ángulo para simular movimiento circular
                luna.setAngulo(luna.getAngulo() + self.VelocidadLuna)

            # MANTENER EL ÁNGULO MENOR A 360 PARA NO ROMPER EL CÓDIGO
                if luna.getAngulo() >= 360:
                    luna.setAngulo(luna.getAngulo() - 360)
        #VOLVER A LLAMAR LA FUNCIÓN
        self.root.after(10, self.MoverEspacio)

if __name__ == "__main__":
    tinker = Tk()
    Ventana = Proyecto(tinker)
    tinker.mainloop()
