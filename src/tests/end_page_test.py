import unittest
import pygame
import sys

class TestEndPage(unittest.TestCase):
    def setUp(self):
        self.click3 = False
        pygame.init()
        self.mx, self.my = pygame.mouse.get_pos()
        self.exit = pygame.Rect(245, 190, 150, 30)
    
    def test_exit(self):
        if self.exit.collidepoint((self.mx, self.my)):
            if self.click3:
                self.assertEqual((pygame.quit(), sys.exit()))