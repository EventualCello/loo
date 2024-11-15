from CUERPOCELESTE import CUERPOCELESTE
from ESTRELLA import ESTRELLA
from LUNA import LUNA
from PLANETA import PLANETA
import pygame
import sys
from tkinter import *
from tkinter import messagebox

pygame.init()

size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Cuerpos Celestes")
running = True
while running:
    #HOLA
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

    # Lógica para actualizar la pantalla aquí

    pygame.display.flip()  # Actualiza el contenido de la ventana

pygame.quit()
sys.exit()

