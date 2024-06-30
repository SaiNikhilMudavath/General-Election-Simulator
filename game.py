import pygame
import sys
import garb as g
import try2 as t 
import main as m

pygame.init()

window=pygame.display.set_mode((1920,1080))
background=pygame.image.load("templates/collage2.jpg")
running = True

font=pygame.font.Font(None,36)
text_surf1=font.render("Play Waste Classification",True,(0,0,0))
text_surf2=font.render("Play Voting Simulation",True,(255,255,255))

while running:
    window.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type==pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y=pygame.mouse.get_pos()
            if 300<mouse_x<630 and 500<mouse_y<550:
                # g.main(window)
                print("x")
                t.intromain(window)
            elif 1380<mouse_x<1680 and 220<mouse_y<240:
                m.main(window)
                
    window.blit(text_surf1,(330,500))
    window.blit(text_surf2,(1400,220))

    pygame.display.flip()

pygame.quit()
sys.exit()