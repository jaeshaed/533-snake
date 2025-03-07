import pygame
import random

pygame.init()

white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
gray = (128, 128, 128)

snake_images = [
    pygame.image.load('11.png'),  # Первое изображение
    pygame.image.load('12.png'),  # Второе изображение
]

fon = pygame.image.load("52.png")
pole = pygame.image.load("42.png")

for i in range(len(snake_images)):
    snake_images[i] = pygame.transform.scale(snake_images[i], (35, 35))

window_width = 800
window_height = 800
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Змейка')

clock = pygame.time.Clock()

snake = [(0, 10), (-1, 10)]
direction = (1, 0)

# Состояние изображений для каждого сегмента змейки
snake_states = [0] * len(snake)

food = (random.randint(0, 19), random.randint(0, 19))

# Размер клетки
cell_size = 35

# Размер поля (в клетках)
grid_size = 20

# Отступы для центрирования поля
offset_x = 50
offset_y = 80

def draw_snake(snake, snake_states):
    for i, segment in enumerate(snake):
        # Получаем текущее изображение для сегмента
        image_index = snake_states[i]
        current_image = snake_images[image_index]
        # Отрисовываем изображение
        window.blit(current_image, (offset_x + segment[0] * cell_size, offset_y + segment[1] * cell_size))

def draw_food(food):
    pygame.draw.rect(window, red, (offset_x + food[0] * cell_size, offset_y + food[1] * cell_size, cell_size, cell_size))

# Основной игровой цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != (0, 1):
                direction = (0, -1)
            elif event.key == pygame.K_DOWN and direction != (0, -1):
                direction = (0, 1)
            elif event.key == pygame.K_LEFT and direction != (1, 0):
                direction = (-1, 0)
            elif event.key == pygame.K_RIGHT and direction != (-1, 0):
                direction = (1, 0)

    # Движение змейки
    new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])

    # Проверка на столкновение с границами
    if new_head[0] < 0 or new_head[0] >= grid_size or new_head[1] < 0 or new_head[1] >= grid_size:
        running = False

    # Проверка на столкновение с самой собой
    if new_head in snake:
        running = False

    # Добавление новой головы
    snake.insert(0, new_head)
    snake_states.insert(0, 0)  # Добавляем состояние для новой головы

    # Проверка на съедание еды
    if new_head == food:
        food = (random.randint(0, grid_size - 1), random.randint(0, grid_size - 1))
    else:
        snake.pop()
        snake_states.pop()  # Удаляем состояние для хвоста

    # Обновление состояний изображений для каждого сегмента
    for i in range(len(snake_states)):
        snake_states[i] = (snake_states[i] + 1) % len(snake_images)  # Циклически меняем изображения

    # Отрисовка
    window.blit(fon, (0, 0))
    window.blit(pole, (offset_x, offset_y, grid_size * cell_size, grid_size * cell_size))
    draw_snake(snake, snake_states)
    draw_food(food)
    pygame.display.flip()

    # Управление FPS
    clock.tick(10)

# Завершение Pygame
pygame.quit()