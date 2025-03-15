import pygame
import random

pygame.init()

# Цвета
white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
gray = (128, 128, 128)
score_font = pygame.font.SysFont("comicsans", 35)

# Загрузка изображений для змейки
snake_images_horizontal = [
    pygame.image.load('graf/11.png'),  # Первое изображение для горизонтального движения
    pygame.image.load('graf/12.png'),  # Второе изображение для горизонтального движения
]

snake_images_vertical = [
    pygame.image.load('graf/9.png'),  # Первое изображение для вертикального движения
    pygame.image.load('graf/10.png'),  # Второе изображение для вертикального движения
]

# Загрузка изображений для поворотов
turn_left_down = pygame.image.load('graf/6.png')  # Поворот из горизонтального вверх
turn_left_up = pygame.image.load('graf/7.png')  # Поворот из горизонтального вниз
turn_right_up = pygame.image.load('graf/8.png')  # Поворот из вертикального вправо
turn_right_down = pygame.image.load('graf/5.png')  # Поворот из вертикального влево

# Загрузка изображения головы и хвоста змейки
snake_head_image = pygame.image.load('graf/head.png')
snake_tail_image = pygame.image.load('graf/tail.png')

# Масштабируем изображения для поворотов
turn_left_down = pygame.transform.scale(turn_left_down, (35, 35))
turn_left_up = pygame.transform.scale(turn_left_up, (35, 35))
turn_right_up = pygame.transform.scale(turn_right_up, (35, 35))
turn_right_down = pygame.transform.scale(turn_right_down, (35, 35))

# Масштабируем изображение головы и хвоста
snake_head_image = pygame.transform.scale(snake_head_image, (35, 35))
snake_tail_image = pygame.transform.scale(snake_tail_image, (35, 35))

# Интерфейс
fon = pygame.image.load("graf/fon.png")
pole = pygame.image.load("graf/pole.png")
muson = pygame.image.load("graf/on.png")
mustarg = pygame.image.load("graf/ontarg.png")
musoff = pygame.image.load("graf/off.png")
musofftarg = pygame.image.load("graf/offtarg.png")
score = pygame.image.load("graf/score.png")

for i in range(len(snake_images_horizontal)):
    snake_images_horizontal[i] = pygame.transform.scale(snake_images_horizontal[i], (35, 35))

for i in range(len(snake_images_vertical)):
    snake_images_vertical[i] = pygame.transform.scale(snake_images_vertical[i], (35, 35))

# Загрузка изображений еды
food_images = [
    pygame.image.load("graf/cherry.png"),
    pygame.image.load("graf/banana.png"),
    pygame.image.load("graf/apple.png"),
    pygame.image.load("graf/watermelon.png"),
    pygame.image.load("graf/blueberry.png")
]

for i in range(len(food_images)):
    food_images[i] = pygame.transform.scale(food_images[i], (35, 35))

# Размеры окна
window_width = 800
window_height = 800
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Змейка')

# Музыка
pygame.mixer.music.load("myson.ogg")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.1)

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

# Состояние музыки
music_on = True

def rotated(image, direction):
    """
    Поворачивает изображение в зависимости от направления.
    """
    if direction == (1, 0):  # Вправо
        return pygame.transform.rotate(image, 270)
    elif direction == (-1, 0):  # Влево
        return pygame.transform.rotate(image, 90)
    elif direction == (0, -1):  # Вверх
        return image
    elif direction == (0, 1):  # Вниз
        return pygame.transform.rotate(image, 180)
    return image

def get_turn_image(prev_dir, current_dir):
    """
    Возвращает изображение для поворота в зависимости от направлений.
    """
    if prev_dir == (1, 0):  # Движение вправо
        if current_dir == (0, -1):  # Поворот вверх
            return turn_left_down
        elif current_dir == (0, 1):  # Поворот вниз
            return turn_left_up
    elif prev_dir == (-1, 0):  # Движение влево
        if current_dir == (0, -1):  # Поворот вверх
            return turn_right_down
        elif current_dir == (0, 1):  # Поворот вниз
            return turn_right_up
    elif prev_dir == (0, -1):  # Движение вверх
        if current_dir == (1, 0):  # Поворот вправо
            return turn_right_up
        elif current_dir == (-1, 0):  # Поворот влево
            return turn_left_up
    elif prev_dir == (0, 1):  # Движение вниз
        if current_dir == (1, 0):  # Поворот вправо
            return turn_right_down
        elif current_dir == (-1, 0):  # Поворот влево
            return turn_left_down
    return None

def draw_snake(snake, snake_directions):
    global animation_counter
    for i, segment in enumerate(snake):
        if i == 0:  # Голова змейки
            rotated_head = rotated(snake_head_image, snake_directions[i])
            window.blit(rotated_head, (offset_x + segment[0] * cell_size, offset_y + segment[1] * cell_size))
        elif i == len(snake) - 1:  # Хвост змейки
            rotated_tail = rotated(snake_tail_image, snake_directions[i])
            window.blit(rotated_tail, (offset_x + segment[0] * cell_size, offset_y + segment[1] * cell_size))
        else:  # Тело змейки
            prev_dir = snake_directions[i - 1]
            current_dir = snake_directions[i]
            turn_image = get_turn_image(prev_dir, current_dir)
            if turn_image:  # Если это поворот
                window.blit(turn_image, (offset_x + segment[0] * cell_size, offset_y + segment[1] * cell_size))
            else:  # Обычное тело
                if current_dir == (1, 0) or current_dir == (-1, 0):  # Горизонтальное движение
                    image_index = (animation_counter + i) % len(snake_images_horizontal)
                    current_image = snake_images_horizontal[image_index]
                else:  # Вертикальное движение
                    image_index = (animation_counter + i) % len(snake_images_vertical)
                    current_image = snake_images_vertical[image_index]
                window.blit(current_image, (offset_x + segment[0] * cell_size, offset_y + segment[1] * cell_size))

def draw_food(food):
    global random_food
    window.blit(random_food, (offset_x + food[0] * cell_size, offset_y + food[1] * cell_size))

def Score(score):
    value = score_font.render("Вам счет: " + str(score), True, (255, 255, 255))
    window.blit(value, [40, 20])

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
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pygame.mouse.get_pos()
            hitboxmusic = pygame.Rect(700, 24, 52, 52)
            if hitboxmusic.collidepoint(mouse_pos):
                music_on = not music_on
                if music_on:
                    pygame.mixer.music.unpause()
                else:
                    pygame.mixer.music.pause()

    # Получаем позицию курсора мыши
    mouse_pos = pygame.mouse.get_pos()
    hitboxmusic = pygame.Rect(700, 24, 52, 52)

    # Определяем, какое изображение кнопки использовать
    if hitboxmusic.collidepoint(mouse_pos):
        if music_on:
            muson_current = mustarg  # Изображение при наведении (музыка включена)
        else:
            muson_current = musofftarg  # Изображение при наведении (музыка выключена)
    else:
        if music_on:
            muson_current = muson  # Обычное изображение (музыка включена)
        else:
            muson_current = musoff  # Обычное изображение (музыка выключена)

    # Движение змейки
    new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])

    snakelenght = len(snake)
    # Проверка на столкновение с границами
    if new_head[0] < 0 or new_head[0] >= grid_size or new_head[1] < 0 or new_head[1] >= grid_size:
        running = False
        continue

    # Проверка на столкновение с самой собой
    if new_head in snake:
        running = False
        continue

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
    window.blit(pole, (offset_x, offset_y))
    window.blit(muson_current, (700, 25))  # Отрисовываем кнопку с учётом наведения и состояния музыки
    Score(snakelenght - 2)
    draw_snake(snake, snake_directions)
    draw_food(food)
    pygame.display.flip()

    # Управление FPS
    clock.tick(10)  # Оставляем FPS как есть

# Завершение Pygame
pygame.quit()