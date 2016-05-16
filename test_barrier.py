import pygame, sys, time
from pygame.locals import *

pygame.init()

window_x = 1000
window_y = 700

window = pygame.display.set_mode((window_x, window_y),0 ,32)
pygame.display.set_caption('test window')

Backgroundcolor = (0, 0, 0)

DESTROY = False

counter = 0
counter_2 = 0
counter_3 = 0

number_barrier = 0

movement_left = False
movement_right = False

position_x_ship = window_x / 2
position_y_ship = window_y - 40

shoot_on = False
shoot_x = position_x_ship + 6
shoot_y = position_y_ship + 3

Clock = pygame.time.Clock()

barrier_normal = pygame.image.load('Barrier_normal.png')
barrier_normal_destroyed = pygame.image.load('Barrier_normal_destroyed.png')

barrier_corner_left = pygame.image.load('Barrier_corner_left.png')
barrier_corner_left_destroyed = pygame.image.load('Barrier_corner_left_destroyed.png')

barrier_corner_right = pygame.image.load('Barrier_corner_right.png')
barrier_corner_right_destroyed = pygame.image.load('Barrier_corner_right_destroyed.png')

ship = pygame.image.load('spaceship.png')

shoot = pygame.image.load('munition.png')

def shootHasHitBarrier1(shootRect, b_1):
	if shootRect['rect'].colliderect(b_1['rect']):
		return True
	else:
		return False

def Print_barrier_1():
	for b_1 in barrier_1:
		window.blit(b_1['surface'], b_1['rect'])

while True: # main game loop
	barrier_1 = []



	for x in range(1, 19):
		new_part_barrier_1 = {'rect':pygame.Rect(0, 0, 20,20),
							  'speed':0,
							  'surface':pygame.transform.scale(barrier_normal, (20, 20)),
			}
		barrier_1.append(new_part_barrier_1)

	shootRect = {'rect': pygame.Rect(100, 0, 3, 9),
				'speed': 200,
				'surface': pygame.transform.scale(shoot, (3, 9)),
				}


	while True:
		counter += 1
		window.fill(Backgroundcolor)
		
		for event in pygame.event.get():
			if event.type == KEYDOWN:
				if event.key == ord('a') or event.key == K_LEFT:
					movement_left = True
					movement_right = False

				elif event.key == ord('d') or event.key == K_RIGHT:
					movement_right = True
					movement_left = False

				if shoot_on == False:

					if event.key == K_SPACE:
						window.blit(shoot, (shoot_x, shoot_y))
						shoot_on = True
						shoot_y = window_y -10
						shoot_x = position_x_ship + 7


				if event.key == K_ESCAPE:
					terminate()

					
				if event.type == KEYUP:
					if event.key == ord('a') or event.key == K_LEFT:
						movement_left = False

					elif event.key == ord ('d') or event.key == K_RIGHT:
						movement_right = False

				if movement_left == True:
					position_x_ship = position_x_ship - 2

				if movement_right == True:
					position_x_ship = position_x_ship + 2

				if position_x_ship == 0:
					position_x_ship = position_x_ship + 2

				if position_x_ship == window_x:
					position_x_ship = position_x_ship - 2

		if shoot_on  == True:
			counter_3 += 1
			if counter_3 == 1:
				shootRect['rect'].move_ip(shoot_x, shoot_y)
			if counter_3 != 1:  
				window.blit(shoot, (shoot_x, shoot_y))
				shoot_y = shoot_y - 10
				shootRect['rect'].move_ip(0, -10)

			if shoot_y == 0:
				shoot_on = False


		window.blit(ship, (position_x_ship, position_y_ship))	

		if counter == 1:
			print(barrier_1)
			for b_1 in barrier_1:
				counter_2 += 1
				x_barrier = counter_2 * 50
				print(x_barrier)
				b_1['rect'].move_ip(x_barrier, 600)

		if counter == 1:
			print(barrier_1)
			print()
			print()

		Print_barrier_1()

		number_barrier = 0

		for b_1 in barrier_1:
#			print(b_1)
			number_barrier += 1
			if shootHasHitBarrier1(shootRect, b_1):
				print('removed #', number_barrier)
				barrier_1.remove(b_1)
				shoot_on = False
				pygame.display.update()
				exit = True

		pygame.display.update()
		Clock.tick(40)