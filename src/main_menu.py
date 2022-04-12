import os
import sys
import pygame
from pygame.locals import *
from game_loop import GameLoop

### Olen käyttänyt pylint-disable:a tässä sillä
### en ymmärrä miksi se huomauttaa tuollaisista
### esim. pygamen init() tai pygame."joku näppäin"
### Jos tälle on jokin hyvä korjaus niin voisitteko laittaa siitä viestiä

MainClock = pygame.time.Clock()
labyrinth = GameLoop()

class Menu:

    def __init__(self):
        self._running = True
        self._screen = None
        self.click = False

    def on_init(self):
        pygame.init() # pylint: disable=no-member
        self._screen = pygame.display.set_mode((640, 480))
        self._running = True
        pygame.display.set_caption("Main Menu")
        os.environ["SDL_VIDEO_CENTERED"] = "1"

    def menu_text(self, text, font, color, surface, x, y): # pylint: disable=invalid-name
        self.textobject = font.render(text, 1, color)
        self.textrect = self.textobject.get_rect()
        self.textrect.topleft = (x,y)
        surface.blit(self.textobject, self.textrect)

    def on_render(self):
        self._screen.fill((39, 39, 39))
        self.fontti = pygame.font.SysFont(None, 25)
        pygame.draw.rect(self._screen, (255, 255, 255), self.game1_button)
        self.menu_text('main menu', self.fontti, (255, 255, 255), self._screen, 285, 20)
        self.menu_text('Labyrintti-peli', self.fontti, (0, 0, 0), self._screen, 260, 127)
        pygame.display.update()

    def on_button(self):
        mx, my = pygame.mouse.get_pos()  # pylint: disable=invalid-name
        self.game1_button = pygame.Rect(245, 120, 150, 30)
        if self.game1_button.collidepoint((mx, my)): # pylint: disable=invalid-name
            if self.click:
                labyrinth.on_execute()

    def events(self):
        self.click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # pylint: disable=no-member
                pygame.quit() # pylint: disable=no-member
                sys.exit()
            if event.type == pygame.KEYDOWN: # pylint: disable=no-member
                if event.key == pygame.K_ESCAPE: # pylint: disable=no-member
                    pygame.quit() # pylint: disable=no-member
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN: # pylint: disable=no-member
                if event.button == 1:
                    self.click = True

    def main_menu(self):
        if self.on_init() is False:
            self._running = False

        while self._running:
            MainClock.tick(60)
            self.on_button()
            self.on_render()
            self.events()

if __name__ == "__main__" :
    theGame = Menu()
    theGame.main_menu()
    