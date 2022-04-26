import pygame
from levels import walls

class Player:
    def __init__(self):
        self.rect = pygame.Rect(32, 32, 16, 16)

    def move(self, dx, dy): # pylint: disable=invalid-name
        if dx != 0: # pylint: disable=invalid-name
            self.advance_single_axis(dx, 0)
        if dy != 0: # pylint: disable=invalid-name
            self.advance_single_axis(0, dy)

    def advance_single_axis(self, dx, dy): # pylint: disable=invalid-name
        self.rect.x += dx # pylint: disable=invalid-name
        self.rect.y += dy # pylint: disable=invalid-name

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
