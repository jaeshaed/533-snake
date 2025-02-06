import pygame
import time
import random

pygame.init()

white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

winWidth = 800
winHeight = 800

win = pygame.display.set_mode((winWidth, winHeight))
clock = pygame.time.Clock()

snakeBlock = 10
snakeSpeed = 15

font = pygame.font.SysFont("Calibri", 25)

def score(score):
    value = font.render(str(score), True, yellow)
    win.blit(value, [0, 0])

def snake(snakeBlock, snakeList):
    for x in snakeList:
        pygame.draw.rect(win, white, [x[0], x[1], snakeBlock, snakeBlock])

def gameLoop():
    gameOver = False
    gameClose = False

    x1 = winWidth / 2
    y1 = winHeight / 2

    x1Change = 0
    y1Change = 0

    snakeList = []
    snakeLenght = 1

    foodx = round(random.randrange(0, winWidth - snakeBlock) / 10.0) * 10.0
    foody = round(random.randrange(0, winHeight - snakeBlock) / 10.0) * 10.0

    while not gameOver:

        while gameClose == True:
            gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1Change = -snakeBlock
                    y1Change = 0
                elif event.key == pygame.K_RIGHT:
                    x1Change = snakeBlock
                    y1Change = 0
                elif event.key == pygame.K_UP:
                    y1Change = -snakeBlock
                    x1Change = 0
                elif event.key == pygame.K_DOWN:
                    y1Change = snakeBlock
                    x1Change = 0

        if x1 >= winWidth or x1 < 0 or y1 >= winHeight or y1 < 0:
            gameClose = True
        
        x1 += x1Change
        y1 += y1Change

        win.fill(black)

        pygame.draw.rect(win, green, [foodx, foody, snakeBlock, snakeBlock])

        snakeHead = []
        snakeHead.append(x1)
        snakeHead.append(y1)
        snakeList.append(snakeHead)

        if len(snakeList) > snakeLenght:
            del snakeList[0]

        for x in snakeList[:-1]:
            if x == snakeHead:
                gameClose = True

        snake(snakeBlock, snakeList)
        score(snakeLenght - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, winWidth - 50 - snakeBlock) / 10.0) * 10.0
            foody = round(random.randrange(0, winHeight - 50 - snakeBlock) / 10.0) * 10.0
            snakeLenght += 1

        clock.tick(snakeSpeed)

    pygame.quit()
    quit()

gameLoop()
