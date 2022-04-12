import os
import sys
import pygame
from levels import *
from player import *

### Olen käyttänyt pylint-disable:a tässä sillä
### en ymmärrä miksi se huomauttaa tuollaisista
### esim. pygamen init() tai pygame."joku näppäin" (pygame.QUIT)
### Jos tälle on jokin hyvä korjaus niin voisitteko laittaa siitä viestiä, kiitos.

clock = pygame.time.Clock()

x = y = 0  # pylint: disable=invalid-name
for row in level:
    for col in row:
        if col == "H":
            Wall((x, y)) # pylint: disable=invalid-name
        if col == "E":
            end_rect = pygame.Rect(x, y, 16, 16)
        x += 16
    y += 16 # pylint: disable=invalid-name
    x = 0 # pylint: disable=invalid-name

player = Player()

class GameLoop:
    width = 640
    height = 480
    def __init__(self):
        self._running = True
        self._screen = None
        #self._image_surf = None

    def on_init(self):
        #pygame.init()
        self._screen = pygame.display.set_mode((self.width, self.height))
        self._running = True
        os.environ["SDL_VIDEO_CENTERED"] = "1"
        pygame.display.set_caption("Find exit!")

    def on_render(self):
        self._screen.fill((79, 79, 79))
        for wall in walls:
            pygame.draw.rect(self._screen, (3, 3, 3), wall.rect)
        pygame.draw.rect(self._screen, (72, 61, 139), end_rect)
        pygame.draw.rect(self._screen, (238, 48, 167), player.rect)
        pygame.display.flip()
        clock.tick(360)

    def on_moving(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]: # pylint: disable=no-member
            player.move(-2, 0)
        if key[pygame.K_RIGHT]: # pylint: disable=no-member
            player.move(2, 0)
        if key[pygame.K_UP]: # pylint: disable=no-member
            player.move(0, -2)
        if key[pygame.K_DOWN]: # pylint: disable=no-member
            player.move(0, 2)

    def on_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # pylint: disable=no-member
                self._running = False
            if event.type == pygame.KEYDOWN: # pylint: disable=no-member
                if event.key == pygame.K_ESCAPE: # pylint: disable=no-member
                    self._running = False

    def on_execute(self):
        if self.on_init() is False:
            self._running = False

        while self._running:
            clock.tick(60)

            if player.rect.colliderect(end_rect):
                #end_page()
                sys.exit()

            self.on_events()
            self.on_moving()
            self.on_render()
