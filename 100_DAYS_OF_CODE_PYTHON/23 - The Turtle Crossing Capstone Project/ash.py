import pygame
import random

# Initialize pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FINISH_LINE_Y = 50
MOVE_INCREMENT = 0.1

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Setup screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Turtle Crossing")

# Game variables
turtle_x = SCREEN_WIDTH // 2
turtle_y = SCREEN_HEIGHT - 50
car_speed = 1
level = 1
clock = pygame.time.Clock()
cars = []


def draw_turtle(x, y):
    pygame.draw.rect(screen, WHITE, (x, y, 20, 20))


def draw_car(x, y):
    pygame.draw.rect(screen, RED, (x, y, 40, 20))


def check_collision(turtle_rect, car_rect):
    return turtle_rect.colliderect(car_rect)


running = True
while running:
    screen.fill((0, 0, 0))

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            turtle_y -= 10

    # Spawn cars
    if len(cars) % 6 == 0:
        cars.append([SCREEN_WIDTH, random.randint(50, SCREEN_HEIGHT - 100), car_speed])

    # Move and draw cars
    for car in cars:
        car[0] -= car[2]
        draw_car(car[0], car[1])

    # Draw turtle
    draw_turtle(turtle_x, turtle_y)

    # Check collisions
    turtle_rect = pygame.Rect(turtle_x, turtle_y, 20, 20)
    for car in cars:
        car_rect = pygame.Rect(car[0], car[1], 40, 20)
        if check_collision(turtle_rect, car_rect):
            running = False

    # Check for level up
    if turtle_y <= FINISH_LINE_Y:
        turtle_y = SCREEN_HEIGHT - 50
        level += 1
        car_speed += MOVE_INCREMENT

    # Update display
    pygame.display.flip()
    clock.tick(60)

# Game over display
font = pygame.font.SysFont(None, 48)
text = font.render("GAME OVER", True, WHITE)
text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
screen.blit(text, text_rect)
pygame.display.flip()

pygame.time.wait(2000)  # Wait for 2 seconds before quitting
pygame.quit()
