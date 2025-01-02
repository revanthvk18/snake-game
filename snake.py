import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
CELL_SIZE = 20
FPS = 10

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Load background image and music
background_image = pygame.image.load("/mnt/data/peakpx.jpg")
background_music = "/mnt/data/mass-kgf-45050.mp3"
pygame.mixer.music.load(background_music)
pygame.mixer.music.play(-1)  # Play music on loop

clock = pygame.time.Clock()

snake = [(100, 100), (90, 100), (80, 100)]
direction = "RIGHT"
fruit_position = (random.randint(0, (WIDTH // CELL_SIZE) - 1) * CELL_SIZE,
                  random.randint(0, (HEIGHT // CELL_SIZE) - 1) * CELL_SIZE)
fruit_color = random.choice([RED, YELLOW])
obstacles = [(random.randint(0, (WIDTH // CELL_SIZE) - 1) * CELL_SIZE,
              random.randint(0, (HEIGHT // CELL_SIZE) - 1) * CELL_SIZE) for _ in range(10)]

score = 0

def draw_snake():
    for segment in snake:
        pygame.draw.rect(screen, GREEN, pygame.Rect(segment[0], segment[1], CELL_SIZE, CELL_SIZE))

def draw_fruit():
    pygame.draw.rect(screen, fruit_color, pygame.Rect(fruit_position[0], fruit_position[1], CELL_SIZE, CELL_SIZE))

def draw_obstacles():
    for obstacle in obstacles:
        pygame.draw.rect(screen, WHITE, pygame.Rect(obstacle[0], obstacle[1], CELL_SIZE, CELL_SIZE))

def check_collision(position):
    if position in snake or position in obstacles or position[0] < 0 or position[1] < 0 or position[0] >= WIDTH or position[1] >= HEIGHT:
        return True
    return False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and direction != "DOWN":
        direction = "UP"
    if keys[pygame.K_DOWN] and direction != "UP":
        direction = "DOWN"
    if keys[pygame.K_LEFT] and direction != "RIGHT":
        direction = "LEFT"
    if keys[pygame.K_RIGHT] and direction != "LEFT":
        direction = "RIGHT"

    head_x, head_y = snake[0]
    if direction == "UP":
        head_y -= CELL_SIZE
    if direction == "DOWN":
        head_y += CELL_SIZE
    if direction == "LEFT":
        head_x -= CELL_SIZE
    if direction == "RIGHT":
        head_x += CELL_SIZE

    new_head = (head_x, head_y)

    if check_collision(new_head):
        pygame.quit()
        sys.exit()

    snake.insert(0, new_head)

    if new_head == fruit_position:
        score += 1
        fruit_position = (random.randint(0, (WIDTH // CELL_SIZE) - 1) * CELL_SIZE,
                          random.randint(0, (HEIGHT // CELL_SIZE) - 1) * CELL_SIZE)
        fruit_color = random.choice([RED, YELLOW])
        while fruit_position in snake or fruit_position in obstacles:
            fruit_position = (random.randint(0, (WIDTH // CELL_SIZE) - 1) * CELL_SIZE,
                              random.randint(0, (HEIGHT // CELL_SIZE) - 1) * CELL_SIZE)
    else:
        snake.pop()

    screen.blit(background_image, (0, 0))  # Draw background image
    draw_snake()
    draw_fruit()
    draw_obstacles()
    pygame.display.flip()
    clock.tick(FPS)
