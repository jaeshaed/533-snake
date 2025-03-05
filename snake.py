import pygame
import sys
import json
pos = 0
nig = 1
block = 0
b_scale = 30

with open('gridMap.json', 'r') as file:
    data = json.load(file)

gridSample = [
 [pos, pos, pos, nig, pos, pos, pos, pos, pos, pos, pos, pos, pos, nig, pos, pos, pos, pos, pos, pos],
 [pos, pos, pos, nig, pos, pos, pos, pos, pos, pos, pos, pos, pos, nig, pos, nig, nig, nig, nig, pos],
 [pos, pos, pos, nig, pos, pos, pos, pos, pos, pos, pos, pos, pos, nig, pos, pos, pos, pos, pos, pos],
 [pos, pos, pos, nig, pos, nig, pos, nig, pos, pos, pos, pos, pos, nig, pos, pos, pos, pos, pos, pos],
 [pos, pos, pos, nig, nig, nig, nig, pos, pos, pos, pos, pos, pos, nig, pos, pos, pos, pos, pos, pos],
 [pos, pos, pos, nig, pos, pos, nig, pos, pos, pos, pos, pos, pos, nig, pos, pos, nig, pos, pos, pos],
 [pos, pos, pos, nig, pos, pos, nig, pos, pos, pos, pos, pos, pos, nig, pos, pos, nig, nig, pos, pos],
 [pos, pos, pos, pos, pos, pos, nig, pos, pos, nig, pos, pos, pos, nig, pos, pos, pos, nig, pos, pos],
 [pos, pos, pos, pos, pos, pos, nig, pos, pos, nig, nig, pos, pos, nig, pos, pos, pos, nig, pos, pos],
 [pos, pos, pos, pos, nig, nig, nig, pos, pos, pos, nig, pos, pos, nig, pos, pos, pos, nig, pos, pos],
 [pos, pos, pos, pos, pos, pos, nig, pos, pos, pos, nig, pos, pos, nig, pos, pos, pos, nig, pos, pos],
 [pos, pos, pos, pos, pos, pos, nig, pos, pos, pos, nig, pos, pos, pos, pos, pos, pos, nig, pos, pos],
 [pos, pos, pos, pos, pos, pos, nig, pos, pos, pos, nig, pos, pos, pos, pos, pos, pos, nig, pos, pos],
 [pos, pos, pos, pos, pos, pos, nig, pos, pos, pos, nig, pos, pos, pos, pos, nig, nig, nig, nig, pos],
 [pos, pos, pos, pos, nig, nig, nig, nig, nig, nig, nig, nig, nig, pos, pos, nig, pos, pos, pos, pos],
 [pos, pos, pos, pos, pos, pos, pos, pos, pos, pos, pos, pos, nig, pos, pos, nig, pos, pos, pos, pos],
 [pos, nig, nig, pos, pos, pos, pos, pos, pos, pos, pos, pos, nig, pos, pos, nig, pos, pos, pos, pos],
 [pos, nig, nig, pos, pos, pos, pos, pos, pos, pos, pos, pos, pos, pos, pos, nig, pos, pos, pos, pos],
 [pos, pos, pos, pos, pos, pos, pos, pos, pos, pos, pos, pos, pos, pos, pos, pos, pos, pos, pos, pos],
 [pos, pos, pos, pos, pos, pos, pos, pos, pos, pos, pos, pos, pos, pos, pos, pos, pos, pos, pos, pos]
]

TempGrid = gridSample

# for i in range(20):
#     grid = [[block] * 20]
#     grid.append([block] * 20)
#     block = randint(0, 1)

def draw():
    x=0
    y=0
    for row in TempGrid:
        for col in TempGrid:
            for variation in TempGrid:
                if pos:
                    wth = 2
                elif nig:
                    wth = 0
            r = pygame.Rect(x,y,b_scale,b_scale)
            pygame.draw.rect(screen, (255, 250, 0), r, wth)
            x = x + b_scale

        y = y + b_scale
        x = 0

pygame.init()

screen = pygame.display.set_mode((800, 800))
draw()
print(data)
n = 0
for i in range(20):
    print(TempGrid[n])
    n +=1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.flip()