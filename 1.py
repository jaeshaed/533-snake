import pygame
import random

pygame.init()

# Цвета
white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
gray = (128, 128, 128)

# Загрузка изображений для змейки
snake_images_horizontal = [
    pygame.image.load('11.png'),  # Первое изображение для горизонтального движения
    pygame.image.load('12.png'),  # Второе изображение для горизонтального движения
]

snake_images_vertical = [
    pygame.image.load('9.png'),  # Первое изображение для вертикального движения
    pygame.image.load('10.png'),  # Второе изображение для вертикального движения
]

# Масштабируем изображения
for i in range(len(snake_images_horizontal)):
    snake_images_horizontal[i] = pygame.transform.scale(snake_images_horizontal[i], (35, 35))

for i in range(len(snake_images_vertical)):
    snake_images_vertical[i] = pygame.transform.scale(snake_images_vertical[i], (35, 35))

fon = pygame.image.load("52.png")
pole = pygame.image.load("42.png")
food_images = [
    pygame.image.load("cherry.png"),
    pygame.image.load("banana.png"),
    pygame.image.load("apple.png"),
    pygame.image.load("watermelon.png"),
    pygame.image.load("bluberry.png")
]

for i in range(len(food_images)):
    food_images[i] = pygame.transform.scale(food_images[i], (35, 35))

# Размеры окна
window_width = 800
window_height = 800
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Змейка')

clock = pygame.time.Clock()

# Змейка
snake = [(0, 10), (-1, 10)]  # Начальный размер змейки
direction = (1, 0)  # Направление движения (по умолчанию вправо)

# Список направлений для каждого сегмента змейки
snake_directions = [direction] * len(snake)

# Глобальный счётчик анимации
animation_counter = 0

food = (random.randint(0, 19), random.randint(0, 19))
random_food = random.choice(food_images)

# Размер клетки
cell_size = 35

# Размер поля (в клетках)
grid_size = 20

# Отступы для центрирования поля
offset_x = 50
offset_y = 80

def draw_snake(snake, snake_directions):
    global animation_counter
    for i, segment in enumerate(snake):
        # Определяем, какое изображение использовать для текущего сегмента
        segment_direction = snake_directions[i]
        if segment_direction == (1, 0) or segment_direction == (-1, 0):  # Горизонтальное движение
            image_index = (animation_counter + i) % len(snake_images_horizontal)
            current_image = snake_images_horizontal[image_index]
        else:  # Вертикальное движение
            image_index = (animation_counter + i) % len(snake_images_vertical)
            current_image = snake_images_vertical[image_index]
        # Отрисовываем изображение
        window.blit(current_image, (offset_x + segment[0] * cell_size, offset_y + segment[1] * cell_size))

def draw_food(food):
   global random_food
   window.blit(random_food, (offset_x + food[0] * cell_size, offset_y + food[1] * cell_size, cell_size, cell_size))

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
    snake_directions.insert(0, direction)  # Сохраняем направление для нового сегмента

    # Проверка на съедание еды
    if new_head == food:
        food = (random.randint(0, grid_size - 1), random.randint(0, grid_size - 1))
        random_food = random.choice(food_images)
    else:
        snake.pop()
        snake_directions.pop()  # Удаляем направление для хвоста

    # Обновление глобального счётчика анимации
    animation_counter += 1

    # Отрисовка
    window.blit(fon, (0, 0))
    window.blit(pole, (offset_x, offset_y, grid_size * cell_size, grid_size * cell_size))
    draw_snake(snake, snake_directions)
    draw_food(food)
    pygame.display.flip()

    # Управление FPS
    clock.tick(10)

# Завершение Pygame
pygame.quit()