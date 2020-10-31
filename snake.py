#snake games

import pygame
import sys
import random
import time


#Error checker
err_ch =pygame.init()
if err_ch[1] > 0:
	print("YOU LOST, you've had {0} errors".format(err_ch[1]))
	sys.exit()
else:
	print("game initialized")

# Colors
red = pygame.Color(255,10,10) #Game Over
green = pygame.Color(10,255,10) #Snake
black = pygame.Color(0,0,0) #score
white = pygame.Color(255,255,255) #background
brown = pygame.Color(255,127,80) #apples

# Play Surface

# Change the title of the snake
pygame.display.set_caption('My First Snake')

# set the size of the map
mapOfGame = pygame.display.set_mode((720,460))

 # fps controller
fpsCntrl = pygame.time.Clock()

 # Variables

snakePosition = [100,100]
snake = [[100,50], [90,50], [80,50]]

foodPosition = [random.randrange(1,72)*10, random.randrange(1,46)*10]
foodSpawn = True

direction = 'RIGHT'
changeto = direction

#game over!

def gameOver():
	myFun = pygame.font.SysFont('monaco',50)
	goSurface = myFun.render('game over mate', 1, red)
	goRect = goSurface.get_rect()
	goRect.midtop = (360, 15)
	mapOfGame.blit(goSurface, goRect)
	pygame.display.flip()
	time.sleep(4)
	pygame.quit()
	#sys.exit()


# Scoreboard
# def showScore():
# 	sFont = pygame.font.SysFont('monaco', 24)
# 	surf
# GAME TIME

while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RIGHT or event.key == ord('d'):
				changeto = 'RIGHT'
			if event.key == pygame.K_LEFT or event.key == ord('a'):
				changeto = 'LEFT'
			if event.key == pygame.K_UP or event.key == ord('w'):
				changeto = 'UP'
			if event.key == pygame.K_DOWN or event.key == ord('s'):
				changeto = 'DOWN'
			if event.key == pygame.K_ESCAPE:
				pygame.event.post(pygame.event.Event(pygame.QUIT))
			
	# Direction check
	if changeto == 'RIGHT' and not direction == 'LEFT':
		direction = 'RIGHT'
	if changeto == 'LEFT' and not direction == 'RIGHT':
		direction = 'LEFT'
	if changeto == 'UP' and not direction == 'DOWN':
		direction = 'UP'
	if changeto == 'DOWN' and not direction == 'UP':
		direction = 'DOWN'
	
	if direction == 'RIGHT':
		snakePosition[0]+=10
	if direction == 'LEFT':
		snakePosition[0]-=10
	if direction == 'UP':
		snakePosition[1]-=10
	if direction == 'DOWN':
		snakePosition[1]+=10

	#Snake body

	snake.insert(0, list(snakePosition))
	if snakePosition[0] == foodPosition[0] and snakePosition[1] == foodPosition[1]:
		foodPosition = [random.randrange(1,72)*10, random.randrange(1,46)*10]
	else:
		snake.pop()

	#graphics!

	mapOfGame.fill(white)
	for posi in snake:
		pygame.draw.rect(mapOfGame, green, pygame.Rect(posi[0], posi[1], 10,10))
	pygame.draw.rect(mapOfGame, brown, pygame.Rect(foodPosition[0], foodPosition[1], 10,10))
	if snakePosition[0] >= 720 or snakePosition[0] <=0:
		gameOver()
	if snakePosition[1] >=460 or snakePosition[1] <=0:
		gameOver()
	for body in snake[1:]:
		if snakePosition[0] == body[0] and snakePosition[1] == body[1]:
			gameOver()

	pygame.display.flip()
	fpsCntrl.tick(30)