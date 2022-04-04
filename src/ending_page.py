import os
import sys
import random
import pygame

# Initialise pygame
os.environ["SDL_VIDEO_CENTERED"] = "1"
pygame.init()

    # Set up the display
pygame.display.set_caption("Get to the red square!")
screen = pygame.display.set_mode((640, 480))

clock = pygame.time.Clock()

def end_page_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x,y)
    surface.blit(textobj, textrect)

fontti = pygame.font.SysFont(None, 20)

click = False

def end_page():
        runnings = False
        while runnings:
            screen.fill((0,0,0))
            end_page_text('Vicotry!', fontti, (255, 255, 255), screen, 285, 20)

            mx, my = pygame.mouse.get_pos()

            to_main_menu = pygame.Rect(245, 120, 150, 30)

            if to_main_menu.collidepoint((mx, my)):
                if click:
                    #main_menu()
                    pass

            pygame.draw.rect(screen, (255, 255, 255), to_main_menu)

            click = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True

            pygame.display.update()
            clock.tick(60)
