import pygame
import sys
import math
# Initialize Pygame
pygame.init()

# Set up the screen
width = 1500
height = 900
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Rotating Wheel")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
WHEEL_COLOR = (150, 150, 150)
SPINNER_COLOR = (50, 50, 50)

# Wheel parameters
wheel_radius = 100
spinner_length = 50
spinner_width = 5

# Main game loop
clock = pygame.time.Clock()
angle = 0  # Initial angle of rotation for the wheel
rad_angle=math.radians(30)
while True:
    screen.fill(WHITE)
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Calculate the center of the screen
    center_x = width // 2
    center_y = height // 2

    # Calculate the position of the wheel's center
    wheel_center_x = center_x
    wheel_center_y = center_y

    # Calculate the position of the spinner
    spinner_x = center_x + wheel_radius * 1 * pygame.math.Vector2(1, 0).rotate(angle).x
    spinner_y = center_y - wheel_radius * 1 * pygame.math.Vector2(1, 0).rotate(angle).y

    # Draw the wheel
    pygame.draw.circle(screen, WHEEL_COLOR, (wheel_center_x, wheel_center_y), wheel_radius)

    # Draw the spinner
    pygame.draw.line(screen, SPINNER_COLOR, (center_x, center_y), (spinner_x, spinner_y), spinner_width)

    # Update angle for next frame
    angle += 2  # Change the rotation speed by adjusting this value

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)
