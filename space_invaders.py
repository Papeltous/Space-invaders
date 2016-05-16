import pygame, sys, time, random
from pygame.locals import *

pygame.init()
pygame.display.set_caption('ventana de prueba')

windowcolor = (0, 0, 0)
TEXTCOLOR = (255, 255, 255)

#funcions creation
#--------------------------------------------------------------------------------------------

def MunitionHasHitBarrier1(MunitionRect, b_1):
    if MunitionRect['rect'].colliderect(b_1['rect']):
        return True
    else:
        return False

def terminate():
    pygame.quit()
    sys.exit()


def Draw_Text(text, font, surface, x, y):
    objtext = font.render(text, 1, TEXTCOLOR)
    rectext = objtext.get_rect()
    rectext.topleft = (x, y)
    surface.blit(objtext, rectext)

def munitionHasHitAlien1(MunitionRect, e_1):
    # You only need to check the colliderect with one enemy, contained in variable e.
    # Return True if collide, False if not collide

    if MunitionRect['rect'].colliderect(e_1['rect']):
        return True
    else:
        return False

def munitionHasHitAlien2(MunitionRect, e_2):
    # You only need to check the colliderect with one enemy, contained in variable e.
    # Return True if collide, False if not collide

    if MunitionRect['rect'].colliderect(e_2['rect']):
        return True
    else:
        return False

def munitionHasHitAlien3(MunitionRect, e_3):
    # You only need to check the colliderect with one enemy, contained in variable e.
    # Return True if collide, False if not collide

    if MunitionRect['rect'].colliderect(e_3['rect']):
        return True
    else:
        return False

def munitionHasHitAlien4(MunitionRect, e_4):
    # You only need to check the colliderect with one enemy, contained in variable e.
    # Return True if collide, False if not collide

    if MunitionRect['rect'].colliderect(e_4['rect']):
        return True
    else:
        return False

def munitionHasHitAlien5(MunitionRect, e_5):
    # You only need to check the colliderect with one enemy, contained in variable e.
    # Return True if collide, False if not collide

    if MunitionRect['rect'].colliderect(e_5['rect']):
        return True
    else:
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

def Print_barrier_1():
    for b_1 in barrier_1:
        window.blit(b_1['surface'], b_1['rect'])

#--------------------------------------------------------------------------------------------

#sprites creation
#--------------------------------------------------------------------------------------------

munition = pygame.image.load('munition.png')    

explocion = pygame.image.load('explocion.png')

spaceship = pygame.image.load('spaceship.png')

spaceship = pygame.transform.scale(spaceship, (36, 24))

enemy_1_1 = pygame.image.load('enemy1.png')
enemy_1_2 = pygame.image.load('enemy1_2.png')

enemy_2 = pygame.image.load('enemy.png')
enemy_2_2 = pygame.image.load('enemy2_2.png')

enemy_3 = pygame.image.load('enemy3.png')
enemy_3_2 = pygame.image.load('enemy3_1.png')

random_boss = pygame.image.load('random_enemy.png')

barrier_normal = pygame.image.load('Barrier_normal.png')
barrier_normal_destroyed = pygame.image.load('Barrier_normal_destroyed.png')

barrier_corner_left = pygame.image.load('Barrier_corner_left.png')
barrier_corner_left_destryed = pygame.image.load('Barrier_corner_left_destroyed.png')

barrier_corner_right = pygame.image.load('Barrier_corner_right.png')
barrier_corner_right_destroyed = pygame.image.load('Barrier_corner_right_destroyed.png')

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

window_x = 700
window_y = 600

#enemys first row
#---------------------------------------------

position_x_enemy_1a_row = window_x / 12

position_y_enemy_1a_row = 20



position_x_spaceship = window_x / 2
position_y_spaceship = window_y - 40

munition_x = position_x_spaceship + 6
munition_y = position_y_spaceship + 3

counter_3 = 0

counter_2 = 0

counter_4 = 0

counter_5 = 0

counter_6 = 0

counter_7 = 0

counter_8 = 0 

counter_2_0 = True

ready_for_explocion = False

window = pygame.display.set_mode((window_x, window_y))
Reloj = pygame.time.Clock()
FPS = 60

# Use pygame font, not System Font
font = pygame.font.Font(None, 24)
font_big = pygame.font.Font(None, 64)

Init = False

right = False

#---------------------------------------------------------------------------------------------

#the game's loop
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
while True:

    barrier_1 = []

    exit = False

    Draw_Text('Space invaders.', font, window, (window_x / 3), (window_y / 3))
    Draw_Text('Press a key for go to the controls.', font, window, (window_x / 3) - 30, (window_y / 3) + 50)
    pygame.display.update()
    waitForPlayerToPressKey()

    window.fill(windowcolor)

    Draw_Text('CONTROLS', font_big, window, window_x/4, (window_y/3) - 50)

    Draw_Text('For you can move you need to press the a and d keys.', font, window, 0, (window_y / 3))
    Draw_Text('For Munition you need to press the key space.', font, window, 0, (window_y / 3) + 50)
    Draw_Text('Press a key to start.', font, window, 0, (window_y / 3) + 100)
    pygame.display.update()
    waitForPlayerToPressKey()

    window.fill(windowcolor)

    Draw_Text('DOWNLOADING...', font, window, window_x/3, window_y/2)

    pygame.display.update()

    enemies_1 = []
    enemies_2 = []
    enemies_3 = []
    enemies_4 = []
    enemies_5 = []

    MunitionRect = {'rect': pygame.Rect(100, 0, 3, 9),
                    'speed': 200,
                    'surface': pygame.transform.scale(munition, (3, 9)),
                    }

    for x in range(1,12):
        new_enemy_1 = {'rect': pygame.Rect(0, 0, 33, 24),
                      'speed': 2,
                      'surface':pygame.transform.scale(enemy_1_1, (33, 24)),

    
                    }

        enemies_1.append(new_enemy_1)


    for x in range(1,12):
        new_enemy_2 = {'rect': pygame.Rect(0, 0, 33, 24),
                      'speed': 2,
                      'surface':pygame.transform.scale(enemy_1_1, (33, 24)),


                    }

        enemies_2.append(new_enemy_2)

    for x in range(1,12):
        new_enemy_3 = {'rect': pygame.Rect(0, 0, 24, 24),
                      'speed': 2,
                      'surface':pygame.transform.scale(enemy_2, (24, 24)),

    
                    }

        enemies_3.append(new_enemy_3)

    for x in range(1,12):
        new_enemy_4 = {'rect': pygame.Rect(0, 0, 36, 24),
                      'speed': 2,
                      'surface':pygame.transform.scale(enemy_3, (36, 24)),

    
                    }

        enemies_4.append(new_enemy_4)

    for x in range(1,12):
        new_enemy_5 = {'rect': pygame.Rect(0, 0, 36, 24),
                      'speed': 2,
                      'surface':pygame.transform.scale(enemy_3, (36, 24)),

    
                    }

        enemies_5.append(new_enemy_5)

    for x in range(1, 19):
        new_part_barrier_1 = {'rect':pygame.Rect(100, 0, 20,20),
                              'speed':0,
                              'surface':pygame.transform.scale(barrier_normal, (20, 20)),
            }

        barrier_1.append(new_part_barrier_1)

    corner_1 = {'rect':pygame.Rect(100,0, 20, 20),
                'speed':0,
                'surface':pygame.transform.scale(barrier_corner_left, (20,20)),
                }
    barrier_1.append(corner_1)

    corner_2 = {'rect':pygame.Rect(100,0, 20, 20),
                'speed':0,
                'surface':pygame.transform.scale(barrier_corner_right, (20,20)),
                }
    barrier_1.append(corner_2)

    counter_3 = 0

    while True:
        window.fill(windowcolor)

        if enemies_1 == [] and enemies_2 == [] and enemies_3 == [] and enemies_4 == [] and enemies_5 == []:
            break

        if counter_3/20 == int(counter_3/3):
            enemy1_actual_true = True

        if not counter_3/20 :
            enemy1_actual_true = False

        if enemy1_actual_true == True:
            enemy1_actual = enemy_1_2

        if enemy1_actual_true == False:
            enemy1_actual = enemy_1_1


        counter_7 = 0

        for e_1 in enemies_1:
            counter_7 += 1

            # If you do a for e_1 in enemies_1, then you have every enemy in e, and you have to call the munitionHasHitAlien1
            # using only one enemy (e) and not the list of all enemies (enemies_1)
            if munitionHasHitAlien1(MunitionRect, e_1):
                enemies_1.remove(e_1)
                munition_on = False
                counter_8 = 0

        counter_7 = 0

        for e_2 in enemies_2:
            counter_7 += 1

            # If you do a for e_2 in enemies_2, then you have every enemy in e, and you have to call the munitionHasHitAlien2
            # using only one enemy (e) and not the list of all enemies (enemies_2)
            if munitionHasHitAlien2(MunitionRect, e_2):
                enemies_2.remove(e_2)
                munition_on = False
                counter_8 = 0

        counter_7 = 0

        for e_3 in enemies_3:
            counter_7 += 1

            # If you do a for e_3 in enemies_3, then you have every enemy in e, and you have to call the munitionHasHitAlien3
            # using only one enemy (e) and not the list of all enemies (enemies_3)
            if munitionHasHitAlien3(MunitionRect, e_3):
                enemies_3.remove(e_3)
                munition_on = False
                counter_8 = 0


        counter_7 = 0

        for e_4 in enemies_4:
            counter_7 += 1

            # If you do a for e_4 in enemies_4, then you have every enemy in e, and you have to call the munitionHasHitAlien4
            # using only one enemy (e) and not the list of all enemies (enemies_4)
            if munitionHasHitAlien4(MunitionRect, e_4):
                enemies_4.remove(e_4)
                munition_on = False
                counter_8 = 0

        counter_7 = 0

        for e_5 in enemies_5:
            counter_7 += 1

            # If you do a for e_5 in enemies_5, then you have every enemy in e, and you have to call the munitionHasHitAlien5
            # using only one enemy (e) and not the list of all enemies (enemies_5)
            if munitionHasHitAlien5(MunitionRect, e_5):
                enemies_5.remove(e_5)
                munition_on = False
                counter_8 = 0

        counter_3 += 1

        counter_5 = 0

        if counter_3 == 2:
            for e_1 in enemies_1[:]:
                counter_5 += window_x/14
                e_1['rect'].move_ip(counter_5, window_y/8 * 1) 

        counter_9 = 0

        if counter_3 == 2:
            for e_2 in enemies_2[:]:
                counter_9 += window_x/14
                e_2['rect'].move_ip(counter_9, window_y/8 * 2)     

        counter_10 = 0

        if counter_3 == 2:
            for e_3 in enemies_3[:]:
                counter_10 += window_x/14
                e_3['rect'].move_ip(counter_10, window_y/8 * 3) 

        counter_11 = 0

        if counter_3 == 2:
            for e_4 in enemies_4[:]:
                counter_11 += window_x/14
                e_4['rect'].move_ip(counter_11, window_y/8 * 4)

        counter_13 = 0

        if counter_3 == 2:
            for e_5 in enemies_5[:]:
                counter_13 += window_x/14
                e_5['rect'].move_ip(counter_13, window_y/8 * 5)

        if counter_3/20 == int(counter_3/20):
            for e_1 in enemies_1:
                e_1['surface'] = pygame.transform.scale(enemy_1_2, (33, 24))

            for e_2 in enemies_2:
                e_2['surface'] = pygame.transform.scale(enemy_1_2, (33, 24))

            for e_3 in enemies_3:
                e_3['surface'] = pygame.transform.scale(enemy_2_2, (24, 24))

            for e_4 in enemies_4:
                e_4['surface'] = pygame.transform.scale(enemy_3_2, (36, 24))

            for e_5 in enemies_5:
                e_5['surface'] = pygame.transform.scale(enemy_3_2, (36, 24))

        if counter_3/40 == int(counter_3/40):
            for e_1 in enemies_1:
                e_1['surface'] = pygame.transform.scale(enemy_1_1, (33, 24))

            for e_2 in enemies_2:
                e_2['surface'] = pygame.transform.scale(enemy_1_1, (33, 24))

            for e_3 in enemies_3:
                e_3['surface'] = pygame.transform.scale(enemy_2, (24, 24))

            for e_4 in enemies_4:
                e_4['surface'] = pygame.transform.scale(enemy_3, (36, 24))

            for e_5 in enemies_5:
                e_5['surface'] = pygame.transform.scale(enemy_3, (36, 24))

        if counter_3/20 == int(counter_3/20):
            for e_1 in enemies_1[:]:
                if right == True:
                    e_1['rect'].move_ip(e_1['speed'] - e_1['speed']*2 , 0)

                elif right == False:
                    e_1['rect'].move_ip(e_1['speed'], 0)

                if e_1['rect'].right == window_x:
                    right = True

                if e_1['rect'].left == 0:
                    right = False
                    for e_1 in enemies_1:
                        e_1['rect'].move_ip(0, 10)

                    for e_2 in enemies_2:
                        e_2['rect'].move_ip(0, 10)

                    for e_3 in enemies_3:
                        e_3['rect'].move_ip(0, 10)

                    for e_4 in enemies_4:
                        e_4['rect'].move_ip(0, 10)

                    for e_5 in enemies_5:
                        e_5['rect'].move_ip(0, 10)

        for e_1 in enemies_1:
            window.blit(e_1['surface'], e_1['rect'])

        if counter_3/20 == int(counter_3/20):
            for e_2 in enemies_2[:]:
                if right == True:
                    e_2['rect'].move_ip(e_2['speed'] - e_2['speed']*2 , 0)

                elif right == False:
                    e_2['rect'].move_ip(e_2['speed'], 0)

                if e_2['rect'].right == window_x:
                    right = True

                if e_2['rect'].left == 0:
                    right = False
                    for e_1 in enemies_1:
                        e_1['rect'].move_ip(0, 10)

                    for e_2 in enemies_2:
                        e_2['rect'].move_ip(0, 10)

                    for e_3 in enemies_3:
                        e_3['rect'].move_ip(0, 10)

                    for e_4 in enemies_4:
                        e_4['rect'].move_ip(0, 10)

                    for e_5 in enemies_5:
                        e_5['rect'].move_ip(0, 10)

        for e_2 in enemies_2:
            window.blit(e_2['surface'], e_2['rect'])        

        if counter_3/20 == int(counter_3/20):
            for e_3 in enemies_3[:]:
                if right == True:
                    e_3['rect'].move_ip(e_3['speed'] - e_3['speed']*2 , 0)

                elif right == False:
                    e_3['rect'].move_ip(e_3['speed'], 0)

                if e_3['rect'].right == window_x:
                    right = True

                if e_3['rect'].left == 0:
                    right = False
                    for e_1 in enemies_1:
                        e_1['rect'].move_ip(0, 10)

                    for e_2 in enemies_2:
                        e_2['rect'].move_ip(0, 10)

                    for e_3 in enemies_3:
                        e_3['rect'].move_ip(0, 10)

                    for e_4 in enemies_4:
                        e_4['rect'].move_ip(0, 10)

                    for e_5 in enemies_5:
                        e_5['rect'].move_ip(0, 10)


        for e_3 in enemies_3:
            window.blit(e_3['surface'], e_3['rect'])        

        if counter_3/20 == int(counter_3/20):
            for e_4 in enemies_4[:]:
                if right == True:
                    e_4['rect'].move_ip(e_4['speed'] - e_4['speed']*2 , 0)

                elif right == False:
                    e_4['rect'].move_ip(e_4['speed'], 0)

                if e_4['rect'].right == window_x:
                    right = True

                if e_4['rect'].left == 0:
                    right = False
                    for e_1 in enemies_1:
                        e_1['rect'].move_ip(0, 10)

                    for e_2 in enemies_2:
                        e_2['rect'].move_ip(0, 10)

                    for e_3 in enemies_3:
                        e_3['rect'].move_ip(0, 10)

                    for e_4 in enemies_4:
                        e_4['rect'].move_ip(0, 10)

                    for e_5 in enemies_5:
                        e_5['rect'].move_ip(0, 10)

        for e_4 in enemies_4:
            window.blit(e_4['surface'], e_4['rect'])        

        if counter_3/20 == int(counter_3/20):
            for e_5 in enemies_5[:]:
                if right == True:
                    e_5['rect'].move_ip(e_5['speed'] - e_5['speed']*2 , 0)

                elif right == False:
                    e_5['rect'].move_ip(e_5['speed'], 0)

                if e_5['rect'].right == window_x:
                    right = True

                if e_5['rect'].left == 0:
                    right = False
                    for e_1 in enemies_1:
                        e_1['rect'].move_ip(0, 10)

                    for e_2 in enemies_2:
                        e_2['rect'].move_ip(0, 10)

                    for e_3 in enemies_3:
                        e_3['rect'].move_ip(0, 10)

                    for e_4 in enemies_4:
                        e_4['rect'].move_ip(0, 10)

                    for e_5 in enemies_5:
                        e_5['rect'].move_ip(0, 10)

        for e_5 in enemies_5:
            window.blit(e_5['surface'], e_5['rect'])        


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

            if event.type == KEYDOWN:
                if event.key == ord('a') or event.key == K_LEFT:
                    movement_left = True
                    movement_right = False

                elif event.key == ord('d') or event.key == K_RIGHT:
                    movement_right = True
                    movement_left = False

                if event.key == ord('q'):
                    exit = True

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
                        munition_y = window_y -10
                        munition_x = position_x_spaceship + 7

        if exit == True:
            break

        if movement_left == True:
            position_x_spaceship = position_x_spaceship - 2

        if movement_right == True:
            position_x_spaceship = position_x_spaceship + 2

        if position_x_spaceship == 0:
            position_x_spaceship = position_x_spaceship + 2

        if position_x_spaceship == window_x:
            position_x_spaceship = position_x_spaceship - 2
        
        if munition_on  == True:
            counter_6 += 1
            if counter_6 != 1:  
                window.blit(munition, (munition_x, munition_y))
                munition_y = munition_y - 10
                MunitionRect['rect'].move_ip(0, -10)

            if munition_y == 0:
                munition_on = False

        window.blit(spaceship, (position_x_spaceship, position_y_spaceship))
        if counter_3 == 1:
            counter_15 = 0
            counter_16 = 0
            for b_1 in barrier_1:
                counter_16 += 1
                if counter_16 < 5 and counter_16 > 0:
                    counter_15 += 1
                    b_1['rect'] = (400 + (counter_15 * 20),450, 20, 20)

                if counter_16 == 4:
                    counter_15 = 0

                if counter_16 < 11 and counter_16 > 4:
                    counter_15 += 1
                    b_1['rect'] = (380 + (counter_15 * 20),470, 20, 20)

                if counter_16 == 10:
                    counter_15 = 0

                if counter_16 < 13 and counter_16 > 10:
                    counter_15 += 1
                    b_1['rect'] =(380 + (counter_15 * 20),490, 20, 20)

                if counter_16 == 12:
                    counter_15 = 0

                if counter_16 < 15 and counter_16 > 12:
                    counter_15 += 1
                    b_1['rect'] = (460 + (counter_15 * 20),490, 20, 20)

                if counter_16 == 14:
                    counter_15 = 0

                if counter_16 < 17 and counter_16 > 14:
                    counter_15 += 1
                    b_1['rect'] = (380 + (counter_15 * 20),510, 20, 20)

                if counter_16 == 16:
                    counter_15 = 0

                if counter_16 < 19 and counter_16 > 16:
                    counter_15 += 1
                    b_1['rect'] = (460 + (counter_15 * 20),510, 20, 20)

                if counter_16 == 18:
                    counter_15 = 0

                if counter_16 < 20 and counter_16 > 18:
                    counter_15 += 1
                    b_1['rect'] = (380 + (counter_15 * 20), 450, 20, 20)

                if counter_16 == 19:
                    counter_15 = 0

                if counter_16 < 21 and counter_16 > 19:
                    counter_15 += 1
                    b_1['rect'] = (480 + (counter_15 * 20),450,20,20)

        Print_barrier_1()

        number_barrier = 0

        for b_1 in barrier_1:
            number_barrier += 1
            if MunitionHasHitBarrier1(MunitionRect, b_1):
                print('removed #', number_barrier, 'with rect:', b_1['rect'])
                print(counter_3)
                print(b_1)
                barrier_1.remove(b_1)
                munition_on = False

        pygame.display.update()
        Reloj.tick(FPS)

    window.fill(windowcolor)
    pygame.display.update()

    Draw_Text('You finish the development version,', font, window, window_x/4, (window_y/6)*2)
    Draw_Text('press a key to return to play :)', font, window, window_x/4, (window_y/6)*3)
    pygame.display.update()
    waitForPlayerToPressKey()

    window.fill(windowcolor)