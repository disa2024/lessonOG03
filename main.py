import pygame
import random

pygame.init()

# Задаем название игры
pygame.display.set_caption("Игра Тир")

# Задаем размеры игрового окна 800х600
screen = pygame.display.set_mode((800, 600))

# Задаём иконку игры
icon = pygame.image.load("pics/icon_1.jpeg")
pygame.display.set_icon(icon)

# Задаем фон игры
background = pygame.image.load("pics/ground.jpg")

# Задаем размер и изображение мишени
aim = pygame.image.load("pics/aim1.png")
aim_width = 80
aim_height = 87

# Прописываем начальное положение мишени
aim_x = random.randint(0, 800 - aim_width)
aim_y = random.randint(0, 600 - aim_height)

# Задаем шрифт для отображения текста
font = pygame.font.Font(None, 36)

# Задаём счетчик очков
score = 0

# Устанавливаем начальное время
start_ticks = pygame.time.get_ticks()

# Задаем игровой процесс
running = True
game_over = False
while running:
    # Рассчитываем оставшееся время
    seconds = (pygame.time.get_ticks() - start_ticks) // 1000
    remaining_time = 10 - seconds
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if aim_x < mouse_x < aim_x + aim_width and aim_y < mouse_y < aim_y + aim_height:
                score += 1
    if remaining_time <= 0:
        game_over = True
        remaining_time = 0

    # Обновляем положение мишени
    if not game_over:
        aim_x = random.randint(0, 800 - aim_width)
        aim_y = random.randint(0, 600 - aim_height)
    # Обновляем фон
    screen.blit(background, (0, 0))
    # Отображаем мишень
    if not game_over:
        screen.blit(aim, (aim_x, aim_y))
    # Отображаем время и очки
    time_text = font.render(f"Time: {remaining_time}", True, (255, 255, 255))
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    # Обновляем время и очки
    screen.blit(time_text, (10, 10))
    screen.blit(score_text, (650, 10))

    pygame.display.update()
    # Задержка для смены позиции мишени
    pygame.time.delay(900)  # 500 миллисекунд

pygame.quit()