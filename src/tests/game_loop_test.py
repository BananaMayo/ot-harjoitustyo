import unittest
import pygame
import sys
from game_loop import GameLoop, end_rect
import end_page

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


endings = end_page.End
class TestGame1(unittest.TestCase):
        def setUp(self):
            self.peli = GameLoop()
            self.sum_coin = 0
            self.coins = [pygame.Rect(550, 14, 19, 19)]
            
        def test_aloituspaikka(self):
            pelaaja = Player()
            self.assertEqual((pelaaja.rect.x,pelaaja.rect.y), (32,32))

        def test_raha(self):
            pelaaja = Player()
            for coin in self.coins:
                if pelaaja.rect.colliderect(coin):
                    self.assertEqual(self.sum_coin, +10)

        def test_ending(self):
            pelaaja = Player()
            if pelaaja.rect.colliderect(end_rect):
                self.assertEqual(endings.end_page())


