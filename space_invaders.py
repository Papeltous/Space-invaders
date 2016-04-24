import pygame, sys, time, random
from pygame.locals import *

pygame.init()
pygame.display.set_caption('ventana de prueva')

windowcolor = (0, 0, 0)
TEXTCOLOR = (255, 255, 255)

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

def munitionHasHitAlien1(MunitionRect, enemies_1):
    for e in enemies_1:
        if MunitionRect['rect'].colliderect(e['rect']):
            return e
        return False

def waitForPlayerToPressKey():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE: # pressing escape quits
                    terminate()
                return

#--------------------------------------------------------------------------------------------

#sprites creation
#--------------------------------------------------------------------------------------------

munition = pygame.image.load('munition.png')    

spaceship = pygame.image.load('spaceship.png')
ShipRect = spaceship.get_rect

enemy_1_1 = pygame.image.load('enemy1.png')
enemy_1_2 = pygame.image.load('enemy1_2.png')
enemy1_actual = enemy_1_1
enemy_1Rect = enemy1_actual.get_rect

enemy_2 = pygame.image.load('enemy.png')
enemy_2_2 = pygame.image.load('enemy2_2.png')
enemy2_actual = enemy_2
enemy_2Rect = enemy2_actual.get_rect

enemy_3 = pygame.image.load('enemy3.png')
enemy_3_2 = pygame.image.load('enemy3_1.png')
enemy3_actual = enemy_3
enemy_3Rect = enemy3_actual.get_rect

random_boss = pygame.image.load('random_enemy.png')


pygame.mixer.music.load('background.mid')

#--------------------------------------------------------------------------------------------


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

counter_3 = 0

counter_2 = 0

counter_4 = 0

counter_5 = 0

counter_6 = 0

counter_2_0 = True

window = pygame.display.set_mode((window_x, window_y))
Reloj = pygame.time.Clock()
FPS = 60

font = pygame.font.SysFont(None, 24)

font_big = pygame.font.SysFont(None, 64)

Init = False

right = False

Draw_Text('Space invaders.', font, window, (window_x / 3), (window_y / 3))
Draw_Text('Press a key for go to the controls.', font, window, (window_x / 3) - 30, (window_y / 3) + 50)
pygame.display.update()
waitForPlayerToPressKey()

window.fill(windowcolor)

Draw_Text('CONTROLS', font_big, window, window_x/4, (window_y/3) - 50)

Draw_Text('For you can move you need to press the a and d keys.', font, window, 0, (window_y / 3))
Draw_Text('For shoot you need to press the key space.', font, window, 0, (window_y / 3) + 50)
Draw_Text('Press a key to start.', font, window, 0, (window_y / 3) + 100)
pygame.display.update()
waitForPlayerToPressKey()

window.fill(windowcolor)

Draw_Text('DOWNLOADING...', font, window, window_x/3, window_y/2)

pygame.display.update()


#---------------------------------------------------------------------------------------------

#the game's loop
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
while True:

    enemies_1 = []
    enemies_2 = []
    enemies_3 = []
    enemies_4 = []
    enemies_5 = []

    MunitionRect = {'rect': pygame.Rect(0, 0, 1, 3),
                    'speed': 100,
                    'surface': pygame.transform.scale(munition, (1, 3)),
                    }

    for x in range(1,25):
        new_enemy_1 = {'rect': pygame.Rect(0, 0, 22, 16),
                      'speed': 1,
                      'surface':pygame.transform.scale(enemy1_actual, (22, 16)),
                    }

        enemies_1.append(new_enemy_1)

        pygame.mixer.music.play(-1, 0.0)

    while True: 

        if counter_3/20 == int(counter_3/3):
            enemy1_actual_true = True

        if not counter_3/20 :
            enemy1_actual_true = False

        if enemy1_actual_true == True:
            enemy1_actual = enemy_1_2

        if enemy1_actual_true == False:
            enemy1_actual = enemy_1_1


        counter_7 = 0

        for e in enemies_1:
            counter_7 += 1
            if munitionHasHitAlien1(MunitionRect, enemies_1):        
                print('bicho', counter_7)
                enemies_1.remove(e)
                print('boom')       

        window.fill(windowcolor)
        counter_3 += 1

        if counter_3 == 2:
            for e in enemies_1[:]:
                counter_5 += window_x/13
                e['rect'].move_ip(counter_5, 100) 


        for e in enemies_1[:]:
            if right == True:
                e['rect'].move_ip(e['speed'] - e['speed']*2 , 0)

            elif right == False:
                e['rect'].move_ip(e['speed'], 0)

            if e['rect'].right == window_x:
                right = True

            if e['rect'].left == 0:
                right = False


        for e in enemies_1:
            window.blit(e['surface'], e['rect'])        

        if counter_3 / 5 == int(counter_3 / 5):

            counter_4 = counter_4 + 1

            if counter == 0:
                n0 = True
            if counter == 1:
                n0 = False

            if counter == 2:
                counter = -1

            if counter_4 / 40 == int(counter_4 / 40):
                position_y_enemy_1a_row = position_y_enemy_1a_row + 5

            counter = counter + 1

            if counter_2 == -20:
                counter_2_0 = True

            if counter_2 == 20:
                counter_2_0 = False

            if counter_2_0 == True:
                counter_2 = counter_2 + 1
            
            if counter_2_0 == False:
                counter_2 = counter_2 - 1

            position_x_enemy_1a_row = position_x_enemy_1a_row + 1
    		
        if munition_on == False:
            munition_x = position_x_spaceship + 7
            munition_y = position_y_spaceship - 3
            MunitionRect['rect'].top = position_y_spaceship
            MunitionRect['rect'].left = position_x_spaceship

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

#-----------------------------------------------------------------------------------------------------------

                if event.key == K_ESCAPE:
                    terminate()

                
            if event.type == KEYUP:
                if event.key == ord('a') or event.key == K_LEFT:
                    movement_left = False

                elif event.key == ord ('d') or event.key == K_RIGHT:
                    movement_right = False

                if munition_on == False:

                    if event.key == K_SPACE:
                        window.blit(munition, (munition_x, munition_y))
                        munition_on = True
                        munition_y = 390
                        munition_x = position_x_spaceship + 7


        if movement_left == True:
            position_x_spaceship = position_x_spaceship - 2

        if movement_right == True:
            position_x_spaceship = position_x_spaceship + 2

        if position_x_spaceship == 0:
            position_x_spaceship = position_x_spaceship + 2

        if position_x_spaceship == window_x:
            position_x_spaceship = position_x_spaceship - 2

#-------------------------------------------------------------------------------------------------------------  

#sprites prints
#-------------------------------------------------------------------------------------------------------------
        
        if munition_on  == True:
            counter_6 += 1
            if counter_6 == 1:
                MunitionRect['rect'].move_ip(munition_x, munition_y)
            if counter_6 != 1:    
                window.blit(munition, (munition_x, munition_y))
                munition_y = munition_y - 10
                MunitionRect['rect'].move_ip(0, -10)

            if munition_y == 0:
                munition_on = False

        window.blit(spaceship, (position_x_spaceship, position_y_spaceship))

#-------------------------------------------------------------------------------------------------------------


        print(FPS)

        pygame.display.update()
        Reloj.tick(FPS)
