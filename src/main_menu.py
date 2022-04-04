import os
import sys
import random
import pygame
from labyrinth import Game1

MainClock = pygame.time.Clock()
from pygame.locals import *

os.environ["SDL_VIDEO_CENTERED"] = "1"
pygame.init()

pygame.display.set_caption("Main Menu")
screen = pygame.display.set_mode((640, 480))

fontti = pygame.font.SysFont(None, 25)

def menu_text(text, font, color, surface, x, y):
    textobject = font.render(text, 1, color)
    textrect = textobject.get_rect()
    textrect.topleft = (x,y)
    surface.blit(textobject, textrect)


click = False

def main_menu():
    while True:

        screen.fill((39, 39, 39))


        menu_text('main menu', fontti, (255, 255, 255), screen, 285, 20)

        mx, my = pygame.mouse.get_pos()

        game1_button = pygame.Rect(245, 120, 150, 30)


        if game1_button.collidepoint((mx, my)):
            if click:
                Game1()

        pygame.draw.rect(screen, (255, 255, 255), game1_button)
        menu_text('Labyrintti-peli', fontti, (0, 0, 0), screen, 260, 127)

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
        MainClock.tick(60)

main_menu()
