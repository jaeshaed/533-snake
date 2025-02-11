import numpy
import pygame
import sys
from random import *

pos = 0
neg = 1
block = 0
b_scale = 30

grid = [[block]*20 for n in range(20)]  # generating clear grid list

def draw():  # randomly revalue "blocks" in grid and draw's grid in pygame / soon drawing the grid will be delated 
    x=0
    y=0
    for row in grid:
        for col in grid:
            block = randrange(5)
            if block >= 1:
                wth = 2
            else:
                wth = 0
            r = pygame.Rect(x,y,b_scale,b_scale)
            pygame.draw.rect(screen, (255, 250, 0), r, wth)
            x = x + b_scale

        y = y + b_scale
        x = 0

pygame.init()

screen = pygame.display.set_mode((800, 800))
draw()
print(grid)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.flip()

# grid = [
#  [pos, pos, pos, neg, pos, pos, pos, pos, pos, pos, pos, pos, pos, neg, pos, pos, pos, pos, pos, pos],
#  [pos, pos, pos, neg, pos, pos, pos, pos, pos, pos, pos, pos, pos, neg, pos, neg, neg, neg, neg, pos],
#  [pos, pos, pos, neg, pos, pos, pos, pos, pos, pos, pos, pos, pos, neg, pos, pos, pos, pos, pos, pos],
#  [pos, pos, pos, neg, pos, neg, pos, neg, pos, pos, pos, pos, pos, neg, pos, pos, pos, pos, pos, pos],
#  [pos, pos, pos, neg, neg, neg, neg, pos, pos, pos, pos, pos, pos, neg, pos, pos, pos, pos, pos, pos],
#  [pos, pos, pos, neg, pos, pos, neg, pos, pos, pos, pos, pos, pos, neg, pos, pos, neg, pos, pos, pos],
#  [pos, pos, pos, neg, pos, pos, neg, pos, pos, pos, pos, pos, pos, neg, pos, pos, neg, neg, pos, pos],
#  [pos, pos, pos, pos, pos, pos, neg, pos, pos, neg, pos, pos, pos, neg, pos, pos, pos, neg, pos, pos],
#  [pos, pos, pos, pos, pos, pos, neg, pos, pos, neg, neg, pos, pos, neg, pos, pos, pos, neg, pos, pos],
#  [pos, pos, pos, pos, neg, neg, neg, pos, pos, pos, neg, pos, pos, neg, pos, pos, pos, neg, pos, pos],
#  [pos, pos, pos, pos, pos, pos, neg, pos, pos, pos, neg, pos, pos, neg, pos, pos, pos, neg, pos, pos],
#  [pos, pos, pos, pos, pos, pos, neg, pos, pos, pos, neg, pos, pos, pos, pos, pos, pos, neg, pos, pos],
#  [pos, pos, pos, pos, pos, pos, neg, pos, pos, pos, neg, pos, pos, pos, pos, pos, pos, neg, pos, pos],
#  [pos, pos, pos, pos, pos, pos, neg, pos, pos, pos, neg, pos, pos, pos, pos, neg, neg, neg, neg, pos],
#  [pos, pos, pos, pos, neg, neg, neg, neg, neg, neg, neg, neg, neg, pos, pos, neg, pos, pos, pos, pos],
#  [pos, pos, pos, pos, pos, pos, pos, pos, pos, pos, pos, pos, neg, pos, pos, neg, pos, pos, pos, pos],
#  [pos, neg, neg, pos, pos, pos, pos, pos, pos, pos, pos, pos, neg, pos, pos, neg, pos, pos, pos, pos],
#  [pos, neg, neg, pos, pos, pos, pos, pos, pos, pos, pos, pos, pos, pos, pos, neg, pos, pos, pos, pos],
#  [pos, pos, pos, pos, pos, pos, pos, pos, pos, pos, pos, pos, pos, pos, pos, pos, pos, pos, pos, pos],
#  [pos, pos, pos, pos, pos, pos, pos, pos, pos, pos, pos, pos, pos, pos, pos, pos, pos, pos, pos, pos]
# ]