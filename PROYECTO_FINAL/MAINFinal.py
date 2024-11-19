from CUERPOCELESTE import CUERPOCELESTE
from ESTRELLA import ESTRELLA
from LUNA import LUNA
from PLANETA import PLANETA
import sys
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
        self.espacio = Canvas(root, bg='black')
        self.espacio.pack(fill=BOTH, expand=True)

        self.btnPlaneta = Button(root, text='Crear Planeta', command=self.CrearPlaneta)
        self.btnPlaneta.pack(side=LEFT)

        self.btnLuna = Button(root, text='Crear Luna', command=self.CrearLuna)
        self.btnPlaneta.pack(side=LEFT)

        self.btnPausa = Button(root, text='Pausar', command=self.Pausar)
        self.btnPausa.pack(side=LEFT)

        self.btnAjustarVelocidadMas = Button(root, text='Mas Velocidad', command=self.AjustarVelocidadMas)
        self.btnAjustarVelocidadMas.pack(side=LEFT)
        self.btnAjustarVelocidadMenos = Button(root, text='Menos Velocidad', command=self.AjustarVelocidadMenos)
        self.btnAjustarVelocidadMenos.pack(side=LEFT)

        self.btnSalir = Button(root, text='Salir', command=root.quit)
        self.btnSalir.pack(side=LEFT)

        self.HacerSol()
        self.Velocidad = 2
        self.MoverPlanetas()

    def HacerSol(self):
        self.espacio.create_oval(Sol.getPosicionX() - 30, Sol.getPosicionY()- 30,Sol.getPosicionX() + 30, Sol.getPosicionY()+ 30,fill='yellow')
    def CrearPlaneta(self):
        """Abre una nueva ventana para ingresar las especificaciones del planeta."""
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

            messagebox.showinfo("Genial", f"Planeta '{nombre}' creado.")

        except ValueError as e:
            messagebox.showerror("Error", str(e))
    def CrearLuna(self):
        return 0

    def Pausar(self):
        Vel=self.Velocidad
        self.Velocidad = 0
        messagebox.showinfo("Pausa", "El juego está pausado. Aceptar para retornar")
        self.Velocidad = Vel
    def AjustarVelocidadMas(self):
        self.Velocidad+=2
    def AjustarVelocidadMenos(self):
        if self.Velocidad>=3:
            self.Velocidad -= 2
        elif self.Velocidad<=2:
            messagebox.showinfo("Error", "La velocidad no puede bajar más")
    def MoverPlanetas(self):
        self.espacio.delete("planetas")  # Limpia los planetas anteriores

        for planeta in self.planetas:
        # Calcula la nueva posición usando trigonometría
            x = Sol.getPosicionX() + planeta.DistanciaAlSol * math.cos(math.radians(planeta.getAngulo()))
            y = Sol.getPosicionY() + planeta.DistanciaAlSol * math.sin(math.radians(planeta.getAngulo()))

            # Dibuja el planeta
            radio = planeta.Diametro/2  # Radio del planeta
            self.espacio.create_oval(x - radio, y - radio, x + radio, y + radio, fill='green', tags="planetas")

            # Actualiza el ángulo para simular movimiento circular
            planeta.setAngulo(planeta.getAngulo()+self.Velocidad)

            if planeta.getAngulo() >= 360:  # Mantiene el ángulo dentro de un rango válido
                planeta.setAngulo(planeta.getAngulo()-360)

    # Llama a esta función nuevamente después de un corto retraso
        self.root.after(10, self.MoverPlanetas)  # Ajusta el tiempo según sea necesario


if __name__ == "__main__":
    tinker = Tk()
    Ventana = Proyecto(tinker)
    tinker.mainloop()


