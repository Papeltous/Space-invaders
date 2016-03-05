import pygame, sys
from pygame.locals import *

pygame.init()
pygame.display.set_caption('ventana de prueva')

windowcolor = (0, 0, 0)
TEXTCOLOR = (255, 255, 255)

#sprites creation
#--------------------------------------------------------------------------------------------

munition = pygame.image.load('munition.png')
spaceship = pygame.image.load('spaceship.png')
enemy_1_1 = pygame.image.load('enemy1.png')
enemy_1_2 = pygame.image.load('enemy1_2.png')
enemy_2 = pygame.image.load('enemy.png')
enemy_2_2 = pygame.image.load('enemy2_2.png')
enemy_3 = pygame.image.load('enemy3.png')
enemy_3_2 = pygame.image.load('enemy3_1.png')
jefe_final = pygame.image.load('random_enemy.png')

#--------------------------------------------------------------------------------------------

#funcions creation
#--------------------------------------------------------------------------------------------

def Dibujar_Text(text, font, superficie, x, y):
    objtext = font.render(text, 1, TEXT)
    rectext = objtext.get_rect()
    rectext.topleft = (x, y)
    superficie.blit(objtext, rectext)

#--------------------------------------------------------------------------------------------

#variables' creation
#--------------------------------------------------------------------------------------------

left = False

n0 = False

counter = -1

munition_on = False
movement_left = False
movement_right = False

window_x = 600
window_y = 400

#enemys first row
#---------------------------------------------

position_x_enemy_1_1a_row = window_x / 12
position_x_enemy_2_1a_row = window_x / 12 * 2
position_x_enemy_3_1a_row = window_x / 12 * 3
position_x_enemy_4_1a_row = window_x / 12 * 4
position_x_enemy_5_1a_row = window_x / 12 * 5
position_x_enemy_6_1a_row = window_x / 12 * 6
position_x_enemy_7_1a_row = window_x / 12 * 7
position_x_enemy_8_1a_row = window_x / 12 * 8
position_x_enemy_9_1a_row = window_x / 12 * 9
position_x_enemy_10_1a_row = window_x / 12 * 10
position_x_enemy_11_1a_row = window_x / 12 * 11

position_y_enemy_1_1a_row = 20
position_y_enemy_2_1a_row = 20
position_y_enemy_3_1a_row = 20
position_y_enemy_4_1a_row = 20
position_y_enemy_5_1a_row = 20
position_y_enemy_6_1a_row = 20
position_y_enemy_7_1a_row = 20
position_y_enemy_8_1a_row = 20
position_y_enemy_9_1a_row = 20
position_y_enemy_10_1a_row = 20
position_y_enemy_11_1a_row = 20

#----------------------------------------------

#enemys second row
#----------------------------------------------
position_x_enemy_1_2a_row = window_x / 12
position_x_enemy_2_2a_row = window_x / 12 * 2
position_x_enemy_3_2a_row = window_x / 12 * 3
position_x_enemy_4_2a_row = window_x / 12 * 4
position_x_enemy_5_2a_row = window_x / 12 * 5
position_x_enemy_6_2a_row = window_x / 12 * 6
position_x_enemy_7_2a_row = window_x / 12 * 7
position_x_enemy_8_2a_row = window_x / 12 * 8
position_x_enemy_9_2a_row = window_x / 12 * 9
position_x_enemy_10_2a_row = window_x / 12 * 10
position_x_enemy_11_2a_row = window_x / 12 * 11

position_y_enemy_1_2a_row = 40
position_y_enemy_2_2a_row = 40
position_y_enemy_3_2a_row = 40
position_y_enemy_4_2a_row = 40
position_y_enemy_5_2a_row = 40
position_y_enemy_6_2a_row = 40
position_y_enemy_7_2a_row = 40
position_y_enemy_8_2a_row = 40
position_y_enemy_9_2a_row = 40
position_y_enemy_10_2a_row = 40
position_y_enemy_11_2a_row = 40

#----------------------------------------------

#enemys third row
#----------------------------------------------
position_x_enemy_1_3a_row = window_x / 12
position_x_enemy_2_3a_row = window_x / 12 * 2
position_x_enemy_3_3a_row = window_x / 12 * 3
position_x_enemy_4_3a_row = window_x / 12 * 4
position_x_enemy_5_3a_row = window_x / 12 * 5
position_x_enemy_6_3a_row = window_x / 12 * 6
position_x_enemy_7_3a_row = window_x / 12 * 7
position_x_enemy_8_3a_row = window_x / 12 * 8
position_x_enemy_9_3a_row = window_x / 12 * 9
position_x_enemy_10_3a_row = window_x / 12 * 10
position_x_enemy_11_3a_row = window_x / 12 * 11

position_y_enemy_1_3a_row = 60
position_y_enemy_2_3a_row = 60
position_y_enemy_3_3a_row = 60
position_y_enemy_4_3a_row = 60
position_y_enemy_5_3a_row = 60
position_y_enemy_6_3a_row = 60
position_y_enemy_7_3a_row = 60
position_y_enemy_8_3a_row = 60
position_y_enemy_9_3a_row = 60
position_y_enemy_10_3a_row = 60
position_y_enemy_11_3a_row = 60


#----------------------------------------------

#enemys fourth row
#----------------------------------------------

position_x_enemy_1_4a_row = window_x / 12
position_x_enemy_2_4a_row = window_x / 12 * 2
position_x_enemy_3_4a_row = window_x / 12 * 3
position_x_enemy_4_4a_row = window_x / 12 * 4
position_x_enemy_4_4a_row = window_x / 12 * 5
position_x_enemy_6_4a_row = window_x / 12 * 6
position_x_enemy_7_4a_row = window_x / 12 * 7
position_x_enemy_8_4a_row = window_x / 12 * 8
position_x_enemy_9_4a_row = window_x / 12 * 9
position_x_enemy_10_4a_row = window_x / 12 * 10
position_x_enemy_11_4a_row = window_x / 12 * 11


position_y_enemy_1_4a_row = 80
position_y_enemy_2_4a_row = 80
position_y_enemy_3_4a_row = 80
position_y_enemy_4_4a_row = 80
position_y_enemy_5_4a_row = 80
position_y_enemy_6_4a_row = 80
position_y_enemy_7_4a_row = 80
position_y_enemy_8_4a_row = 80
position_y_enemy_9_4a_row = 80
position_y_enemy_10_4a_row = 80
position_y_enemy_11_4a_row = 80

#----------------------------------------------

#enemys fifth row
#----------------------------------------------

position_x_enemy_1_5a_row = window_x / 12
position_x_enemy_2_5a_row = window_x / 12 * 2
position_x_enemy_3_5a_row = window_x / 12 * 3
position_x_enemy_4_5a_row = window_x / 12 * 4
position_x_enemy_5_5a_row = window_x / 12 * 5
position_x_enemy_6_5a_row = window_x / 12 * 6
position_x_enemy_7_5a_row = window_x / 12 * 7
position_x_enemy_8_5a_row = window_x / 12 * 8
position_x_enemy_9_5a_row = window_x / 12 * 9
position_x_enemy_10_5a_row = window_x / 12 * 10
position_x_enemy_11_5a_row = window_x / 12 * 11

position_y_enemy_1_5a_row = 100
position_y_enemy_2_5a_row = 100
position_y_enemy_3_5a_row = 100
position_y_enemy_4_5a_row = 100
position_y_enemy_5_5a_row = 100
position_y_enemy_6_5a_row = 100
position_y_enemy_7_5a_row = 100
position_y_enemy_8_5a_row = 100
position_y_enemy_9_5a_row = 100
position_y_enemy_10_5a_row = 100
position_y_enemy_11_5a_row = 100

#----------------------------------------------

position_x_spaceship = window_x / 2
position_y_spaceship = window_y - 10

munition_x = position_x_spaceship + 6
munition_y = position_y_spaceship

window = pygame.display.set_mode((window_x, window_y))
Reloj = pygame.time.Clock()
FPS = 40
font = pygame.font.SysFont(None, 24)

#---------------------------------------------------------------------------------------------

#the game's loop
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
while True:
    window.blit(spaceship, (position_x_spaceship, position_y_spaceship))
    window.blit(enemy_1_1, (position_x_enemy_1_1a_row, position_y_enemy_1_1a_row))
    window.blit(munition, (munition_x, munition_y))

    while True:
        counter = counter + 1

        if munition_on == False:
            munition_x = position_x_spaceship + 6
            munition_y = position_y_spaceship

        if position_x_enemy_1_1a_row == 20:
            left = True

        if position_x_enemy_1_1a_row == window_x - 20:
            left = False

        if left == True:
            position_x_enemy_1_1a_row = position_x_enemy_1_1a_row + 1

        if left == False:
            position_x_enemy_1_1a_row = position_x_enemy_1_1a_row - 1

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

#spaceship's movement
#-----------------------------------------------------------------------------------------------------------


            if event.type == KEYDOWN:
                if event.key == ord('a') or event.key == K_LEFT:
                    movement_left = True
                    movement_right = False

                elif event.key == ord('d') or event.key == K_RIGHT:
                    movement_right = True
                    movement_left = False

                
            if event.type == KEYUP:
                if event.key == ord('a') or event.key == K_LEFT:
                    movement_left = False

                elif event.key == ord ('d') or event.key == K_RIGHT:
                    movement_right = False

                if event.key == K_SPACE:
                    window.blit(munition, (munition_x, munition_y))
                    munition_on = True
                    munition_y = 390
                    munition_x = position_x_spaceship + 6

        if movement_left == True:
            position_x_spaceship = position_x_spaceship - 2

        if movement_right == True:
            position_x_spaceship = position_x_spaceship + 2
#-------------------------------------------------------------------------------------------------------------

#sprites prints
#-------------------------------------------------------------------------------------------------------------
        window.fill(windowcolor)
        if counter == 0:
            n0 = True
        if counter == 20:
            n0 = False

        if counter == 39:
            counter = -1

        if n0 == True:
            window.blit(enemy_1_1, (position_x_enemy_1_1a_row, position_y_enemy_1_1a_row))

        if n0 == False:
            window.blit(enemy_1_2, (position_x_enemy_1_1a_row, position_y_enemy_1_1a_row))

        if munition_on  == True:
            window.blit(munition, (munition_x, munition_y))
            munition_y = munition_y - 5

            if munition_y == 0:
                munition_on = False

        window.blit(spaceship, (position_x_spaceship, position_y_spaceship))

#-------------------------------------------------------------------------------------------------------------

        pygame.display.update()
        Reloj.tick(FPS)
