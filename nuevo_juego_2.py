import pygame, sys
from pygame.locals import *

pygame.init()
pygame.display.set_caption('pantalla de prueva')

COLORDEPANTALLA = (0, 0, 0)
COLORDETEXTO = (255, 255, 255)

#Creación de "sprites"
#--------------------------------------------------------------------------------------------

nave = pygame.image.load('nave.png')
enemigo_1_1 = pygame.image.load('enemigo1.png')
enemigo_1_2 = pygame.image.load('enemigo1_2.png')
enemigo_2 = pygame.image.load('enemigo.png')
enemigo_2_2 = pygame.image.load('enemigo2_2.png')
enemigo_3 = pygame.image.load('enemigo3.png')
enemigo_3_2 = pygame.image.load('enemigo3_1.png')
jefe_final = pygame.image.load('enemigo_final.png')

#--------------------------------------------------------------------------------------------

#creacion de defs
#--------------------------------------------------------------------------------------------

def Dibujar_Texto(texto, fuente, superficie, x, y):
    objtexto = fuente.render(texto, 1, COLORDETEXTO)
    rectexto = objtexto.get_rect()
    rectexto.topleft = (x, y)
    superficie.blit(objtexto, rectexto)

#--------------------------------------------------------------------------------------------

#Creacion de variables
#--------------------------------------------------------------------------------------------

izquierda = False

movimiento_izquierda = False
movimiento_derecha = False

pantalla_x = 600
pantalla_y = 400

#enemigos primera fila
#---------------------------------------------

posicion_x_enemigo_1_1a_fila = pantalla_x / 12
posicion_x_enemigo_2_1a_fila = pantalla_x / 12 * 2
posicion_x_enemigo_3_1a_fila = pantalla_x / 12 * 3
posicion_x_enemigo_4_1a_fila = pantalla_x / 12 * 4
posicion_x_enemigo_5_1a_fila = pantalla_x / 12 * 5
posicion_x_enemigo_6_1a_fila = pantalla_x / 12 * 6
posicion_x_enemigo_7_1a_fila = pantalla_x / 12 * 7
posicion_x_enemigo_8_1a_fila = pantalla_x / 12 * 8
posicion_x_enemigo_9_1a_fila = pantalla_x / 12 * 9
posicion_x_enemigo_10_1a_fila = pantalla_x / 12 * 10
posicion_x_enemigo_11_1a_fila = pantalla_x / 12 * 11

posicion_y_enemigo_1_1a_fila = 20
posicion_y_enemigo_2_1a_fila = 20
posicion_y_enemigo_3_1a_fila = 20
posicion_y_enemigo_4_1a_fila = 20
posicion_y_enemigo_5_1a_fila = 20
posicion_y_enemigo_6_1a_fila = 20
posicion_y_enemigo_7_1a_fila = 20
posicion_y_enemigo_8_1a_fila = 20
posicion_y_enemigo_9_1a_fila = 20
posicion_y_enemigo_10_1a_fila = 20
posicion_y_enemigo_11_1a_fila = 20

#----------------------------------------------

#enemigos segunda fila
#----------------------------------------------
posicion_x_enemigo_1_2a_fila = pantalla_x / 12
posicion_x_enemigo_2_2a_fila = pantalla_x / 12 * 2
posicion_x_enemigo_3_2a_fila = pantalla_x / 12 * 3
posicion_x_enemigo_4_2a_fila = pantalla_x / 12 * 4
posicion_x_enemigo_5_2a_fila = pantalla_x / 12 * 5
posicion_x_enemigo_6_2a_fila = pantalla_x / 12 * 6
posicion_x_enemigo_7_2a_fila = pantalla_x / 12 * 7
posicion_x_enemigo_8_2a_fila = pantalla_x / 12 * 8
posicion_x_enemigo_9_2a_fila = pantalla_x / 12 * 9
posicion_x_enemigo_10_2a_fila = pantalla_x / 12 * 10
posicion_x_enemigo_11_2a_fila = pantalla_x / 12 * 11

posicion_y_enemigo_1_2a_fila = posicion_y_enemigo_2_2a_fila = posicion_y_enemigo_3_2a_fila = posicion_y_enemigo_4_2a_fila = posicion_y_enemigo_5_2a_fila = posicion_y_enemigo_6_2a_fila = posicion_y_enemigo_7_2a_fila = posicion_y_enemigo_8_2a_fila = posicion_y_enemigo_9_2a_fila = posicion_y_enemigo_10_2a_fila =posicion_y_enemigo_11_2a_fila = 40

#----------------------------------------------

#enemigos tercera fila
#----------------------------------------------
posicion_x_enemigo_1_3a_fila = pantalla_x / 12
posicion_x_enemigo_2_3a_fila = pantalla_x / 12 * 2
posicion_x_enemigo_3_3a_fila = pantalla_x / 12 * 3
posicion_x_enemigo_4_3a_fila = pantalla_x / 12 * 4
posicion_x_enemigo_5_3a_fila = pantalla_x / 12 * 5
posicion_x_enemigo_6_3a_fila = pantalla_x / 12 * 6
posicion_x_enemigo_7_3a_fila = pantalla_x / 12 * 7
posicion_x_enemigo_8_3a_fila = pantalla_x / 12 * 8
posicion_x_enemigo_9_3a_fila = pantalla_x / 12 * 9
posicion_x_enemigo_10_3a_fila = pantalla_x / 12 * 10
posicion_x_enemigo_11_3a_fila = pantalla_x / 12 * 11

posicion_y_enemigo_1_3a_fila = 60
posicion_y_enemigo_2_3a_fila = 60
posicion_y_enemigo_3_3a_fila = 60
posicion_y_enemigo_4_3a_fila = 60
posicion_y_enemigo_5_3a_fila = 60
posicion_y_enemigo_6_3a_fila = 60
posicion_y_enemigo_7_3a_fila = 60
posicion_y_enemigo_8_3a_fila = 60
posicion_y_enemigo_9_3a_fila = 60
posicion_y_enemigo_10_3a_fila = 60
posicion_y_enemigo_11_3a_fila = 60


#----------------------------------------------

#enemigos cuarta fila
#----------------------------------------------

posicion_x_enemigo_1_4a_fila = pantalla_x / 12
posicion_x_enemigo_2_4a_fila = pantalla_x / 12 * 2
posicion_x_enemigo_3_4a_fila = pantalla_x / 12 * 3
posicion_x_enemigo_4_4a_fila = pantalla_x / 12 * 4
posicion_x_enemigo_4_4a_fila = pantalla_x / 12 * 5
posicion_x_enemigo_6_4a_fila = pantalla_x / 12 * 6
posicion_x_enemigo_7_4a_fila = pantalla_x / 12 * 7
posicion_x_enemigo_8_4a_fila = pantalla_x / 12 * 8
posicion_x_enemigo_9_4a_fila = pantalla_x / 12 * 9
posicion_x_enemigo_10_4a_fila = pantalla_x / 12 * 10
posicion_x_enemigo_11_4a_fila = pantalla_x / 12 * 11


posicion_y_enemigo_1_4a_fila = 80
posicion_y_enemigo_2_4a_fila = 80
posicion_y_enemigo_3_4a_fila = 80
posicion_y_enemigo_4_4a_fila = 80
posicion_y_enemigo_5_4a_fila = 80
posicion_y_enemigo_6_4a_fila = 80
posicion_y_enemigo_7_4a_fila = 80
posicion_y_enemigo_8_4a_fila = 80
posicion_y_enemigo_9_4a_fila = 80
posicion_y_enemigo_10_4a_fila = 80
posicion_y_enemigo_11_4a_fila = 80

#----------------------------------------------

#enemigos quinta fila
#----------------------------------------------

posicion_x_enemigo_1_5a_fila = pantalla_x / 12
posicion_x_enemigo_2_5a_fila = pantalla_x / 12 * 2
posicion_x_enemigo_3_5a_fila = pantalla_x / 12 * 3
posicion_x_enemigo_4_5a_fila = pantalla_x / 12 * 4
posicion_x_enemigo_5_5a_fila = pantalla_x / 12 * 5
posicion_x_enemigo_6_5a_fila = pantalla_x / 12 * 6
posicion_x_enemigo_7_5a_fila = pantalla_x / 12 * 7
posicion_x_enemigo_8_5a_fila = pantalla_x / 12 * 8
posicion_x_enemigo_9_5a_fila = pantalla_x / 12 * 9
posicion_x_enemigo_10_5a_fila = pantalla_x / 12 * 10
posicion_x_enemigo_11_5a_fila = pantalla_x / 12 * 11

posicion_y_enemigo_1_5a_fila = 100
posicion_y_enemigo_2_5a_fila = 100
posicion_y_enemigo_3_5a_fila = 100
posicion_y_enemigo_4_5a_fila = 100
posicion_y_enemigo_5_5a_fila = 100
posicion_y_enemigo_6_5a_fila = 100
posicion_y_enemigo_7_5a_fila = 100
posicion_y_enemigo_8_5a_fila = 100
posicion_y_enemigo_9_5a_fila = 100
posicion_y_enemigo_10_5a_fila = 100
posicion_y_enemigo_11_5a_fila = 100

#----------------------------------------------
posicion_x_nave = pantalla_x / 2
posicion_y_nave = pantalla_y -10

PANTALLA = pygame.display.set_mode((pantalla_x, pantalla_y))
disparos = 100
Reloj = pygame.time.Clock()
FPS = 40
fuente = pygame.font.SysFont(None, 30)

#---------------------------------------------------------------------------------------------

#bucle del juego
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
while True:
    PANTALLA.blit(nave, (posicion_x_nave, posicion_y_nave))
    PANTALLA.blit(enemigo_1_1, (posicion_x_enemigo_1_1a_fila, posicion_y_enemigo_1_1a_fila))
    while True:
        PANTALLA.fill(COLORDEPANTALLA)
 
        PANTALLA.blit(nave, (posicion_x_nave, posicion_y_nave))
        PANTALLA.blit(enemigo_1_1, (posicion_x_enemigo_1_1a_fila, posicion_y_enemigo_1_1a_fila))

        if posicion_x_enemigo_1_1a_fila == 20:
            izquierda = True

        if posicion_x_enemigo_1_1a_fila == pantalla_x - 20:
            izquierda = False

        if izquierda == True:
            posicion_x_enemigo_1_1a_fila = posicion_x_enemigo_1_1a_fila + 1

        if izquierda == False:
            posicion_x_enemigo_1_1a_fila = posicion_x_enemigo_1_1a_fila - 1

        print (posicion_x_enemigo_1_1a_fila)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

#movimiento del personaje
#-----------------------------------------------------------------------------------------------------------


            if event.type == KEYDOWN:
                if event.key == ord('a') or event.key == K_LEFT:
                    movimiento_izquierda = True
                    movimiento_derecha = False

                elif event.key == ord('d') or event.key == K_RIGHT:
                    movimiento_derecha = True
                    movimiento_izquierda = False

            if event.type == KEYUP:
                if event.key == ord('a') or event.key == K_LEFT:
                    movimiento_izquierda = False

                elif event.key == ord ('d') or event.key == K_RIGHT:
                    movimiento_derecha = False

        if movimiento_izquierda == True:
            posicion_x_nave = posicion_x_nave - 1

        if movimiento_derecha == True:
            posicion_x_nave = posicion_x_nave + 1
#-------------------------------------------------------------------------------------------------------------

#creacion enemigos
#-------------------------------------------------------------------------------------------------------------



#-------------------------------------------------------------------------------------------------------------
        pygame.display.update()
        Reloj.tick(FPS)
