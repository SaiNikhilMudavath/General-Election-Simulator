import pygame
import sys
import garb as g
# Initialize Pygame
pygame.init()

# Set the dimensions of the screen
# screen_width = 1920
# screen_height = 1080
# screen = pygame.display.set_mode((screen_width, screen_height))
# pygame.display.set_caption("Waste Management Game")

def intromain(screen):
    back_image=pygame.image.load("intro.png")
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    font = pygame.font.Font(None, 36)
    level1_text = font.render("Level 1", True, BLACK)
    level2_text = font.render("Level 2", True, BLACK)
    level1_rect = level1_text.get_rect()
    level2_rect = level2_text.get_rect()
    level1_rect.centerx = 1920 // 4
    level1_rect.centery = 950
    level2_rect.centerx = 3 * 1920 // 4
    level2_rect.centery = 950
    run=True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type==pygame.MOUSEBUTTONDOWN:
                    pos=pygame.mouse.get_pos()
                    if level1_rect.collidepoint(pos):
                        g.main(screen,2.5)
                    elif level2_rect.collidepoint(pos):
                        g.main(screen,1.5)
        screen.blit(back_image, (0, 0))
        screen.blit(level1_text, level1_rect)
        screen.blit(level2_text, level2_rect)
        pygame.display.update()