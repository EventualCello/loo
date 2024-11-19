from CUERPOCELESTE import CUERPOCELESTE
from ESTRELLA import ESTRELLA
from LUNA import LUNA
from PLANETA import PLANETA
import pygame
import sys
from tkinter import *
from tkinter import messagebox
pygame.init()
Planetas = 0
Sol = ESTRELLA()


size = (800, 600)
pantallaPrincipal = pygame.display.set_mode(size)
pygame.display.set_caption("Cuerpos Celestes")
running = True
paused = False


root = Tk()
root.geometry('600x600+400+100')
root.title('PAUSA')
root.config(bg='dark blue')
root.resizable(width=False, height=False)

def AñadirPlaneta():

    global Planetas
    Planetas += 1
    pygame.draw.circle(pantallaPrincipal, (82, 183, 136),(Sol.getPosicionX()+Planetas*50, Sol.getPosicionY()) , 15)

def QuitarPausa():
    global paused
    root.quit()
    paused = False
def AbrirPausa():

    lblEscribir = Label(root, text='ESCRIBIR', width=42)
    lblEscribir.grid(row=1, column=1)
    lblContenido = Label(root, text='Contenido', width=42)
    lblContenido.grid(row=1, column=2)
    '''
    txtEscribir = Text(root, height=30, width=35, bg='white')
    txtEscribir.grid(row=2, column=1)
    txtContenido = Text(root, height=30, width=35, bg='white')
    txtContenido.grid(row=2, column=2)

    btnEscribir = Button(root, text='Escribir', width=10, bg='light green', command=escribir_en_archivo)
    btnEscribir.grid(row=3, column=1)
    btnContenido = Button(root, text='Contenido', width=10, bg='pink', command=leer_archivo)
    btnContenido.grid(row=3, column=2)'''
    '''PLANETA'''

    btnCerrar = Button(root, text='Cerrar', width=10, bg='red', command=QuitarPausa)
    btnCerrar.grid(row=3, column=1)
    root.mainloop()

while running:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                paused = True
                AbrirPausa()


    #RECORDAR QUE CUANDO PEDIMOS UNA POSICIÓN, ES EN X,Y, ASÍ MISMO, HAY QUE USAR COLORES BÁSICOS POR SER RGB
    pygame.draw.circle(pantallaPrincipal, (255,255,0), Sol.ActualizarPosicion(), 30)
    AñadirPlaneta()
    pygame.display.flip()
    clock = pygame.time.Clock()
    clock.tick(24)  #FPS

pygame.quit()
sys.exit()