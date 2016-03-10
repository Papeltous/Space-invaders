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

def terminate():
    pygame.quit()
    sys.exit()


def Draw_Text(text, font, surface, x, y):
    objtext = font.render(text, 1, TEXTCOLOR)
    rectext = objtext.get_rect()
    rectext.topleft = (x, y)
    surface.blit(objtext, rectext)

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

position_x_enemy_1a_row = window_x / 12

position_y_enemy_1a_row = 20



position_x_spaceship = window_x / 2
position_y_spaceship = window_y - 10

munition_x = position_x_spaceship + 6
munition_y = position_y_spaceship

counter_2 = 0

counter_2_0 = True

window = pygame.display.set_mode((window_x, window_y))
Reloj = pygame.time.Clock()
FPS = 40
font = pygame.font.SysFont(None, 24)

#---------------------------------------------------------------------------------------------

#the game's loop
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
while True:
    window.blit(spaceship, (position_x_spaceship, position_y_spaceship))
    window.blit(munition, (munition_x, munition_y))

    while True:
        window.fill(windowcolor)

        if counter_2 == -30:
            counter_2_0 = True

        if counter_2 == 20:
            counter_2_0 = False


        if counter_2_0 == True:
            counter_2 = counter_2 + 1
        
        if counter_2_0 == False:
            counter_2 = counter_2 - 1

        position_x_enemy_1a_row = position_x_enemy_1a_row + 1

        for caca in range(1,13):
            position_y_enemy_1a_row = 20
            position_x_enemy_1a_row = window_x/13 * caca
            position_x_enemy_1a_row = position_x_enemy_1a_row + counter_2
            if n0 == True:
                window.blit(enemy_1_1, (position_x_enemy_1a_row, position_y_enemy_1a_row))

            if n0 == False:
                window.blit(enemy_1_2, (position_x_enemy_1a_row, position_y_enemy_1a_row))

            position_y_enemy_1a_row = position_y_enemy_1a_row + 30

            if n0 == True:
                window.blit(enemy_1_1, (position_x_enemy_1a_row, position_y_enemy_1a_row))

            if n0 == False:
                window.blit(enemy_1_2, (position_x_enemy_1a_row, position_y_enemy_1a_row))



        if counter == 0:
            n0 = True
        if counter == 20:
            n0 = False

        if counter == 39:
            counter = -1


        counter = counter + 1

        if munition_on == False:
            munition_x = position_x_spaceship + 6
            munition_y = position_y_spaceship

        for event in pygame.event.get():
#spaceship's movement
#-----------------------------------------------------------------------------------------------------------
            if event.type == KEYDOWN:
                if event.key == ord('a') or event.key == K_LEFT:
                    movement_left = True
                    movement_right = False

                elif event.key == ord('d') or event.key == K_RIGHT:
                    movement_right = True
                    movement_left = False

                if event.key == K_ESCAPE:
                    terminate()

                
            if event.type == KEYUP:a
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
        
        if munition_on  == True:
            window.blit(munition, (munition_x, munition_y))
            munition_y = munition_y - 5

            if munition_y == 0:
                munition_on = False

        window.blit(spaceship, (position_x_spaceship, position_y_spaceship))

#-------------------------------------------------------------------------------------------------------------

        pygame.display.update()
        Reloj.tick(FPS)