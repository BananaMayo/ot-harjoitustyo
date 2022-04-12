import pygame
import os
import sys
from levels import *
from player import *

clock = pygame.time.Clock()

x = y = 0
for row in level:
    for col in row:
        if col == "H":
            Wall((x, y))
        if col == "E":
            end_rect = pygame.Rect(x, y, 16, 16)
        x += 16
    y += 16
    x = 0

player = Player()

class GameLoop:
    width = 640
    height = 480
    
    def __init__(self):
        self._running = True
        self._screen = None
        #self._image_surf = None
        

    def on_init(self):
        pygame.init()
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

    def on_cleanup(self):
        pygame.quit()
    

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while self._running:
            clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self._running = False

            if player.rect.colliderect(end_rect):
                #end_page()
                pygame.quit()
                sys.exit()

            key = pygame.key.get_pressed()
            if key[pygame.K_LEFT]:
                player.move(-2, 0)
            if key[pygame.K_RIGHT]:
                player.move(2, 0)
            if key[pygame.K_UP]:
                player.move(0, -2)
            if key[pygame.K_DOWN]:
                player.move(0, 2)

            self.on_render()
                    

      
