import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the game window
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong")

# Set up the colors
black = (0, 0, 0)
white = (255, 255, 255)

# Set up the paddles and ball
paddle_width = 15
paddle_height = 100
ball_size = 20

# Paddle positions
paddle1_x = 50
paddle1_y = (screen_height - paddle_height) // 2
paddle2_x = screen_width - 50 - paddle_width
paddle2_y = (screen_height - paddle_height) // 2

# Ball position and velocity
ball_x = screen_width // 2
ball_y = screen_height // 2
ball_speed_x = 5
ball_speed_y = 5

# Paddle speed
paddle_speed = 5

# Main game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Get keys pressed
    keys = pygame.key.get_pressed()

    # Move paddle 1 (AWSD)
    if keys[pygame.K_w] and paddle1_y > 0:
        paddle1_y -= paddle_speed
    if keys[pygame.K_s] and paddle1_y < screen_height - paddle_height:
        paddle1_y += paddle_speed

    # Move paddle 2 (Arrow keys)
    if keys[pygame.K_UP] and paddle2_y > 0:
        paddle2_y -= paddle_speed
    if keys[pygame.K_DOWN] and paddle2_y < screen_height - paddle_height:
        paddle2_y += paddle_speed

    # Move the ball
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Ball collision with top and bottom
    if ball_y <= 0 or ball_y >= screen_height - ball_size:
        ball_speed_y *= -1

    # Ball collision with paddles
    if (paddle1_x < ball_x < paddle1_x + paddle_width and
            paddle1_y < ball_y < paddle1_y + paddle_height):
        ball_speed_x *= -1

    if (paddle2_x < ball_x < paddle2_x + paddle_width and
            paddle2_y < ball_y < paddle2_y + paddle_height):
        ball_speed_x *= -1

    # Ball out of bounds
    if ball_x < 0 or ball_x > screen_width:
        ball_x = screen_width // 2
        ball_y = screen_height // 2
        ball_speed_x *= -1

    # Clear the screen
    screen.fill(black)

    # Draw the paddles and ball
    pygame.draw.rect(screen, white, (paddle1_x, paddle1_y, paddle_width, paddle_height))
    pygame.draw.rect(screen, white, (paddle2_x, paddle2_y, paddle_width, paddle_height))
    pygame.draw.ellipse(screen, white, (ball_x, ball_y, ball_size, ball_size))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)
