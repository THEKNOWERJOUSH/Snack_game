# Made By Shaheen <abdelazizshaheen162@gmail.com> For Python Workshop In Cic
#forked by YLabdelraouf <Youssefi_i06103@cic-cairo.com>For Python Workshop In Cic

import pygame
import random
import os

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 600, 400
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Colors
BGCOLOR = (0, 0, 255)
TEXT_COLOR = (255, 255, 179)
FOOD_COLOR = (0,0,0)
SNAKE_COLOR = (255, 250, 240)

# Snake properties
SNAKE_SIZE = 20
SNAKE_SPEED = 20
SNAKE_BODY = [(WIDTH / 2, HEIGHT / 2)]
SNAKE_DIRECTION = (1, 0)

# Food properties
FOOD_SIZE = 20
FOOD_EXTRA=30
food_pos = (random.randint(0, WIDTH - FOOD_SIZE), random.randint(0, HEIGHT - FOOD_SIZE))
food_EXTEA = (random.randint(0, WIDTH - FOOD_EXTRA), random.randint(0, HEIGHT - FOOD_EXTRA))

# Score
score = 0
highest_score = 0

# Load font
font = pygame.font.Font(None, 36)

# Function to display score
def display_score():
    score_text = font.render("Score: " + str(score), True, TEXT_COLOR)
    WINDOW.blit(score_text, (10, 10))

# Function to display highest score
def display_highest_score():
    highest_score_text = font.render("Highest Score: " + str(highest_score), True, TEXT_COLOR)
    WINDOW.blit(highest_score_text, (WIDTH - highest_score_text.get_width() - 10, 10))

# Function to reset game
def reset_game():
    global SNAKE_BODY, SNAKE_DIRECTION, score, food_pos
    SNAKE_BODY = [(WIDTH / 2, HEIGHT / 2)]
    SNAKE_DIRECTION = (1, 0)
    score = 0
    food_pos = (random.randint(0, WIDTH - FOOD_SIZE), random.randint(0, HEIGHT - FOOD_SIZE))
    shake_screen()

# Function to reset game
def shake_screen():
    shake_intensity = 10
    shake_duration = 1  # in seconds
    start_time = pygame.time.get_ticks()

    while pygame.time.get_ticks() - start_time < shake_duration * 1000:
        dx = random.randint(-shake_intensity, shake_intensity)
        dy = random.randint(-shake_intensity, shake_intensity)
        pygame.draw.rect(WINDOW, SNAKE_COLOR, (WIDTH // 2 + dx, HEIGHT // 2 + dy, 50, 50))  # Example object
        pygame.display.update()
# Main game loop
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Change direction based on key presses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w or event.key == pygame.K_UP and SNAKE_DIRECTION != (0, 1):
                SNAKE_DIRECTION = (0, -1)
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s and SNAKE_DIRECTION != (0, -1):
                SNAKE_DIRECTION = (0, 1)
            elif event.key == pygame.K_LEFT or event.key == pygame.K_a and SNAKE_DIRECTION != (1, 0):
                SNAKE_DIRECTION = (-1, 0)
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d and SNAKE_DIRECTION != (-1, 0):
                SNAKE_DIRECTION = (1, 0)

    # Move the snake
    new_head = (SNAKE_BODY[0][0] + SNAKE_SPEED * SNAKE_DIRECTION[0],
                SNAKE_BODY[0][1] + SNAKE_SPEED * SNAKE_DIRECTION[1])
    SNAKE_BODY.insert(0, new_head)

    # Check for collision with food
    if pygame.Rect(new_head, (SNAKE_SIZE, SNAKE_SIZE)).colliderect(pygame.Rect(food_pos, (FOOD_SIZE, FOOD_SIZE))):
        score += 1
        if score > highest_score:
            highest_score = score
        food_pos = (random.randint(0, WIDTH - FOOD_SIZE), random.randint(0, HEIGHT - FOOD_SIZE))
    else:
        SNAKE_BODY.pop()

    # Check for collision with walls or itself
    if (SNAKE_BODY[0][0] < 0 or SNAKE_BODY[0][0] >= WIDTH or
        SNAKE_BODY[0][1] < 0 or SNAKE_BODY[0][1] >= HEIGHT or
        len(SNAKE_BODY) != len(set(SNAKE_BODY))):
        highest_score=score
        reset_game()

    # Draw everything
    WINDOW.fill(BGCOLOR)
    pygame.draw.rect(WINDOW, FOOD_COLOR, (*food_pos, FOOD_SIZE, FOOD_SIZE))

    for segment in SNAKE_BODY:
        pygame.draw.rect(WINDOW, SNAKE_COLOR, (*segment, SNAKE_SIZE, SNAKE_SIZE))
    if score>5:
        SNAKE_SPEED=30
    if score>10:
        SNAKE_SPEED=20
        WIDTH, HEIGHT = 550, 350
        WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
    if score>15:
        SNAKE_SPEED=30
        WIDTH, HEIGHT = 550, 350
        WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
       # SNAKE_COLOR = (0, 0, 0)
    if score>20:
        SNAKE_SPEED=30
        WIDTH, HEIGHT = 500, 300
        WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
        SNAKE_COLOR = (0, 0, 0)

    
   





    display_score()
    display_highest_score()
    pygame.display.update()
    clock.tick(10)



pygame.quit()

