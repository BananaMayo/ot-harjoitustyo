import time
import os
import pygame
from levels import walls, Wall, level
from player import Player
import end_page

GameClock = pygame.time.Clock()
ending = end_page.End()

"""
Tämä luo sienät peliin ja sijoittaa uloskäynnin labyrinttiin
'H' = seinä
'E' = uloskäynti
"""
X = Y = 0
for row in level:
    for col in row:
        if col == "H":
            Wall((X, Y))
        if col == "E":
            end_rect = pygame.Rect(X, Y, 16, 16)
        X += 16
    Y += 16
    X = 0

player = Player()

class GameLoop:
    sum_coin = 0
    Player_time = 0
    """
    Pelin MazeGame luokka, sisältää useampia funktioita

    Pelissä näkyy labyrintti ja uloskäynti sekä kerättävät
    kolikot, myös kolikoiden määrä ja aika näkyy
    """
    width = 640
    height = 480
    def __init__(self):
        """
        Funktio alustaa kolikot

        Näytön sekä pelin boolean-arvot määriteltynä

        Kolikoiden sijainnit listassa
        Kolikoiden summa on 0, kasvaa aina kymmenellä
        """
        self._running = True
        self._screen = None

        self.coin_image = pygame.image.load('src/coin/coin_0.png')
        self.coins = [pygame.Rect(550, 14, 19, 19),
        pygame.Rect(590, 14, 19, 19),pygame.Rect(510, 14, 19, 19),
        pygame.Rect(470, 14, 19, 19),pygame.Rect(430, 14, 19, 19),
        pygame.Rect(390, 14, 19, 19),pygame.Rect(15, 64, 19, 19),
        pygame.Rect(50, 188, 19, 19),pygame.Rect(348, 190, 19, 19),
        pygame.Rect(606, 45, 19, 19),pygame.Rect(606, 109, 19, 19),
        pygame.Rect(606, 173, 19, 19),pygame.Rect(590, 77, 19, 19),
        pygame.Rect(590, 140, 19, 19),pygame.Rect(590, 205, 19, 19),
        pygame.Rect(550, 206, 19, 19),pygame.Rect(510, 206, 19, 19),
        pygame.Rect(464, 206, 19, 19),pygame.Rect(462, 142, 19, 19),
        pygame.Rect(462, 79, 19, 19),pygame.Rect(511, 46, 19, 19),
        pygame.Rect(558, 79, 19, 19),pygame.Rect(558, 142, 19, 19),
        pygame.Rect(526, 174, 19, 19),pygame.Rect(494, 121, 19, 19),
        pygame.Rect(527, 79, 19, 19),pygame.Rect(527, 142, 19, 19),
        pygame.Rect(497, 283, 19, 19),pygame.Rect(14, 446, 19, 19),
        pygame.Rect(157, 316, 19, 19),pygame.Rect(538, 446, 19, 19),
        pygame.Rect(382, 270, 19, 19),pygame.Rect(336, 445, 19, 19),
        pygame.Rect(255, 16, 19, 19)
        ]

    def on_init(self):
        """
        Näytön alustus ja otsikko
        """
        self._screen = pygame.display.set_mode((self.width, self.height))
        self._running = True
        os.environ["SDL_VIDEO_CENTERED"] = "1"
        pygame.display.set_caption("Find exit!")

    def game_text(self, text, font, color, surface, x, y): # pylint: disable=invalid-name
        """
        Pelin tekstiä varten tehdyt määrittelyt

        Funktion avulla pelissä näkyy kolikoiden
        määrä sekä aika
        """
        self.textobject = font.render(text, 1, color) # pylint: disable=attribute-defined-outside-init
        self.textrect = self.textobject.get_rect() # pylint: disable=attribute-defined-outside-init
        self.textrect.topleft = (x,y)
        surface.blit(self.textobject, self.textrect)

    def on_render(self):
        """
        Näytön värit, fontti, teksti, kolikot, pelaajan hahmo ja uloskäynti

        Näytön virkistys
        """
        self._screen.fill((79, 79, 79))
        self.fontti = pygame.font.SysFont(None, 20) # pylint: disable=attribute-defined-outside-init
        for wall in walls:
            pygame.draw.rect(self._screen, (3, 3, 3), wall.rect)
        pygame.draw.rect(self._screen, (72, 61, 139), end_rect)
        pygame.draw.rect(self._screen, (238, 48, 167), player.rect)
        for _c in self.coins:
            self._screen.blit(self.coin_image,(_c[0], _c[1]))
        self.game_text('Coins: '+str(self.sum_coin), self.fontti, (255,215,0), self._screen, 4, 2)
        self.game_text('Time: '+f'{self.elapsed_time:.1f}', self.fontti, (255,215,0), self._screen, 85, 2)
        pygame.display.flip()
        GameClock.tick(360)

    def on_moving(self):
        """
        Näppäinten toiminnot, pelin hahmo liikkuu +-2 y tai x
        suuntaan riippuen painikkeesta

        Hahmoa liikutetaan nuolinäppäimillä
        """
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
        """
        Events; poistuminen ruksilla tai ESC-painikkeella
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # pylint: disable=no-member
                self._running = False
            if event.type == pygame.KEYDOWN: # pylint: disable=no-member
                if event.key == pygame.K_ESCAPE: # pylint: disable=no-member
                    self._running = False


    def on_execute(self):
        """
        Pelin käynnistyminen, kutsuu aikaisemmin
        määriteltyjä funktioita toimiakseen

        Kolikoiden toiminta määriteltynä, summa += 10, osuman
        jälkeen kolikko poistetaan

        Uloskäynti määriteltynä, peli päättyy kun hahmo osuu uloskäyntiin
        ja pelaaja uudelleenohjataan lopetussivulle
        """

        if self.on_init() is False:
            self._running = False

        self.start_time = time.time()

        while self._running:
            GameClock.tick(60)

            self.elapsed_time = time.time() - self.start_time

            for _c in self.coins:
                if player.rect.colliderect(_c):
                    GameLoop.sum_coin += 10
                    self.coins.remove(_c)

            if player.rect.colliderect(end_rect):
                GameLoop.Player_time += self.elapsed_time
                ending.end_page()

            self.on_events()
            self.on_moving()
            self.on_render()
