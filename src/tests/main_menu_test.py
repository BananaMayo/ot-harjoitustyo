import unittest
import pygame
import sys
import main_menu
import game_loop

class TestMainMenu(unittest.TestCase):
    def setUp(self):
        self.click = False
        pygame.init()
        self.labyrinth = game_loop.GameLoop()
    
    def test_main_to_game(self):
        mx, my = pygame.mouse.get_pos()
        self.game1_button = pygame.Rect(245, 120, 150, 30)
        if self.game1_button.collidepoint((mx, my)):
            if self.click:
               self.assertEqual(self.labyrinth.on_execute())
