import os
import sys
#import random
import pygame

def Game1():
    os.environ["SDL_VIDEO_CENTERED"] = "1"
    pygame.init()
    pygame.display.set_caption("Get to the red square!")
    screen = pygame.display.set_mode((640, 480))
    
    walls = []

    class Player(object):
        def __init__(self):
            self.rect = pygame.Rect(32, 32, 16, 16)

        def move(self, dx, dy):
            if dx != 0:
                self.advance_single_axis(dx, 0)
            if dy != 0:
                self.advance_single_axis(0, dy)

        def advance_single_axis(self, dx, dy):           
            self.rect.x += dx
            self.rect.y += dy
        
            for wall in walls:
                if self.rect.colliderect(wall.rect):
                    if dx > 0: 
                        self.rect.right = wall.rect.left
                    if dx < 0: 
                        self.rect.left = wall.rect.right
                    if dy > 0: 
                        self.rect.bottom = wall.rect.top
                    if dy < 0: 
                        self.rect.top = wall.rect.bottom  
    class Wall(object):
        def __init__(self, pos):
            walls.append(self)
            self.rect = pygame.Rect(pos[0], pos[1], 16, 16) 
    player = Player() 
    clock = pygame.time.Clock()
    level = [
        "HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH",
        "HHH   H   H           H                H",
        "H   H   H HHHHHH H HH   HHHHHHHHHHHHHH H",
        "HH HHHHH       H  H H H H   H       H  H",
        "H   H        HHHH H H HHH H H HHHHH H HH",
        "H HHH  HHHH       H       H H H   H H  H",
        "H   H   H H H   HHHHH   HHHHH H H H HH H",
        "HH  H H   H   HHH     H     H H H H H  H",
        "H   HHH HHH   H H HHH H  H  H H H H H HH",
        "H       H     H H  H  H     H H H H H  H",
        "HHH H H   HHHHH HH H H   HH H H HHH HH H",
        "H H   H  HH        H  HH H  H H     H  H",
        "H H   HHHH   HHH HHHH  H  H H HHHHHHH HH",
        "H HH  H    H  H  H   HHH HH H          H",
        "H H      HHHH H HHHH     H  HHHHHHHHHHHH",
        "H   H    H  HHH    H   H H             H",
        "H    HHHHH      HH   HHH H HHH  HHHH   H",
        "H    H       HHHH        HHHHHH    HH  H",
        "H H HH  HHH  H H  HHHHHHH     H     H  H",
        "H HH    H    H HHHH  H    H  HHHHHH H  H",
        "H H  HHH   HH          H  HHHH    H H  H",
        "H   H HH  H   HHHHHHH HHH       H H H  H",
        "H H H H  HH   H     H H H    HHHH H H  H",
        "H    HH H HHH   HHHHH   H   H     H H  H",
        "HH HHH        HH     H  HH   HHH H  H  H",
        "H  H    H HH HH  HHH  HH HHHHH H H H   H",
        "H   HHH H H HH      H H     HH   H     H",
        "H     HHH H  HHHHHH H HHHHH   H  HH H  H",
        "H HH     HH         H       H  E   H   H",
        "HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH",
    ]

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

    running = True
    while running:

        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

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

        screen.fill((79, 79, 79))
        for wall in walls:
            pygame.draw.rect(screen, (3, 3, 3), wall.rect)
        pygame.draw.rect(screen, (72, 61, 139), end_rect)
        pygame.draw.rect(screen, (238, 48, 167), player.rect)
        pygame.display.flip()
        clock.tick(360)




