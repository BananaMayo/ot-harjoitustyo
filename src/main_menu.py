import os
import sys
import pygame
from game_loop import GameLoop

### Olen käyttänyt pylint-disable:a tässä sillä
### en ymmärrä miksi se huomauttaa tuollaisista
### esim. pygamen init() tai pygame."joku näppäin"
### Jos tälle on jokin hyvä korjaus niin voisitteko laittaa siitä viestiä

### 'defined outside __init__' tätä en ymmärrä josta pylint valittaa?

MainClock = pygame.time.Clock()
labyrinth = GameLoop()

class Menu:
    """
    Luokka, jonka avulla peli käynnistyy. Luo pääsivun josta
    pääsee navigoimaan itsensä peliin.
    """
    def __init__(self):
        """
        Pääsivun alustus
        """
        self._running = True
        self._screen = None
        self.click = False

    def on_init(self):
        """
        Pygamen alustus ja näytön koon asetukset
        """
        pygame.init() # pylint: disable=no-member
        self._screen = pygame.display.set_mode((640, 480))
        self._running = True
        pygame.display.set_caption("Main Menu")
        os.environ["SDL_VIDEO_CENTERED"] = "1"

    def menu_text(self, text, font, color, surface, x, y): # pylint: disable=invalid-name
        """
        Funktio määrittää lisättävän tekstin

        Tämän avulla teksti näkyy pääsivulla
        """
        self.textobject2 = font.render(text, 1, color) # pylint: disable=attribute-defined-outside-init
        self.textrect = self.textobject2.get_rect() # pylint: disable=attribute-defined-outside-init
        self.textrect.topleft = (x,y)
        surface.blit(self.textobject2, self.textrect)

    def on_render(self):
        """
        Funktio renderöi pääsivun ilmeen

        Lisää tekstiä sekä luo painikkeen peliä varten
        """
        self._screen.fill((39, 39, 39))
        self.fontti = pygame.font.SysFont(None, 25) # pylint: disable=attribute-defined-outside-init
        self.fontti2 = pygame.font.SysFont(None, 30) # pylint: disable=attribute-defined-outside-init
        self.edge_for_button = pygame.Rect(242.5, 117.5, 155, 36.5) # pylint: disable=attribute-defined-outside-init
        pygame.draw.rect(self._screen, (0, 0, 0), self.edge_for_button)
        pygame.draw.rect(self._screen, (117, 117, 117), self.game1_button)
        self.menu_text('Welcome!', self.fontti2, (255, 255, 255), self._screen, 270, 30)
        self.menu_text('Press the button to start the game', self.fontti, (117, 117, 117), self._screen, 176, 85)
        self.menu_text('MazeGame', self.fontti, (0, 0, 0), self._screen, 273, 127)
        pygame.display.update()

    def on_button(self):
        """
        Funktio määrittää hiiren painalluksen toiminnon
        peli-painikkeen kohdalla

        Painallus käynnistää pelin
        """
        mx, my = pygame.mouse.get_pos()  # pylint: disable=invalid-name
        self.game1_button = pygame.Rect(245, 120, 150, 30) # pylint: disable=attribute-defined-outside-init
        if self.game1_button.collidepoint((mx, my)): # pylint: disable=invalid-name
            if self.click:
                labyrinth.on_execute()

    def events(self):
        """
        Events osio, tässä määriytyy mitä kukin
        painike tekee pelissä
        """
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
        """
        Funktio kutsuu aiempia funktioita jotta pääsivun
        sekä pelin saa toimimaan
        """
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
    