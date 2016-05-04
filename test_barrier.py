import pygame, sys
from pygame.locals import *

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 300),0 ,32)
pygame.display.set_caption('test window')

Backgroundcolor = (0, 0, 0)

DESTROY = False

counter = 0

Clock = pygame.time.Clock()

barrier_normal = pygame.image.load('Barrier_normal.png')
barrier_normal_destroyed = pygame.image.load('Barrier_normal_destroyed.png')

barrier_corner_left = pygame.image.load('Barrier_corner_left.png')
barrier_corner_left_destroyed = pygame.image.load('Barrier_corner_left_destroyed.png')

barrier_corner_right = pygame.image.load('Barrier_corner_right.png')
barrier_corner_right_destroyed = pygame.image.load('Barrier_corner_right_destroyed.png')

while True: # main game loop
	DISPLAYSURF.fill(Backgroundcolor)

	counter += 1

	print(counter)

	if counter/10 == int(counter/10):
		DESTROY = True

	if counter/20 == int(counter/20):
		DESTROY = False


	if DESTROY == False:
		DISPLAYSURF.blit(barrier_corner_left, (29 ,30))
		DISPLAYSURF.blit(barrier_normal, (49, 30))
		DISPLAYSURF.blit(barrier_normal, (69, 30))
		DISPLAYSURF.blit(barrier_normal, (89, 30))
		DISPLAYSURF.blit(barrier_normal, (109, 30))
		DISPLAYSURF.blit(barrier_corner_right, (129, 30))

		DISPLAYSURF.blit(barrier_normal, (29 ,50))
		DISPLAYSURF.blit(barrier_normal, (49, 50))
		DISPLAYSURF.blit(barrier_normal, (69, 50))
		DISPLAYSURF.blit(barrier_normal, (89, 50))
		DISPLAYSURF.blit(barrier_normal, (109 ,50))
		DISPLAYSURF.blit(barrier_normal, (129, 50))	

		DISPLAYSURF.blit(barrier_normal, (29 ,70))
		DISPLAYSURF.blit(barrier_normal, (49, 70))
		DISPLAYSURF.blit(barrier_normal, (109 ,70))
		DISPLAYSURF.blit(barrier_normal, (129, 70))	

		DISPLAYSURF.blit(barrier_normal, (29 ,90))
		DISPLAYSURF.blit(barrier_normal, (49, 90))
		DISPLAYSURF.blit(barrier_normal, (109 ,90))
		DISPLAYSURF.blit(barrier_normal, (129, 90))

	if DESTROY == True:
		DISPLAYSURF.blit(barrier_corner_left_destroyed, (29 ,30))
		DISPLAYSURF.blit(barrier_normal_destroyed, (49, 30))
		DISPLAYSURF.blit(barrier_normal_destroyed, (69, 30))
		DISPLAYSURF.blit(barrier_normal_destroyed, (89, 30))
		DISPLAYSURF.blit(barrier_normal_destroyed, (109, 30))
		DISPLAYSURF.blit(barrier_corner_right_destroyed, (129, 30))

		DISPLAYSURF.blit(barrier_normal_destroyed, (29 ,50))
		DISPLAYSURF.blit(barrier_normal_destroyed, (49, 50))
		DISPLAYSURF.blit(barrier_normal_destroyed, (69, 50))
		DISPLAYSURF.blit(barrier_normal_destroyed, (89, 50))
		DISPLAYSURF.blit(barrier_normal_destroyed, (109 ,50))
		DISPLAYSURF.blit(barrier_normal_destroyed, (129, 50))	

		DISPLAYSURF.blit(barrier_normal_destroyed, (29 ,70))
		DISPLAYSURF.blit(barrier_normal_destroyed, (49, 70))
		DISPLAYSURF.blit(barrier_normal_destroyed, (109 ,70))
		DISPLAYSURF.blit(barrier_normal_destroyed, (129, 70))	

		DISPLAYSURF.blit(barrier_normal_destroyed, (29 ,90))
		DISPLAYSURF.blit(barrier_normal_destroyed, (49, 90))
		DISPLAYSURF.blit(barrier_normal_destroyed, (109 ,90))
		DISPLAYSURF.blit(barrier_normal_destroyed, (129, 90))

	pygame.display.update()
	Clock.tick(20)