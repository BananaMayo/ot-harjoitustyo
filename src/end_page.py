import os
import sys
import pygame
import game_loop

EndClock = pygame.time.Clock()
class End: # pylint: disable=too-many-instance-attributes
    """Pelin loppusivun luokka

    Loppusivulla näkyy pelattu aika ja kerättyjen
    kolikoiden summa

    Exit-painike ja Restart-painike
    """
    def __init__(self):
        """
        Näytön sekä pelin boolean-arvot määriteltynä
        """
        self._running = True
        self._screen = None
        self.click3 = False

    def _on_init(self):
        """
        Näytön alustus ja otsikko
        """
        os.environ["SDL_VIDEO_CENTERED"] = "1"
        self._screen = pygame.display.set_mode((640, 480))
        self._running = True
        pygame.display.set_caption("VICTORY!")

    def end_page_text(self, text, font, color, surface, X, Y): # pylint: disable=invalid-name
        """Sivun tekstiä varten tehdyt määrittelyt

        Funktion avulla sivulla näkyy tekstit
        """
        self.textobj = font.render(text, 1, color) # pylint: disable=attribute-defined-outside-init
        self.textrect = self.textobj.get_rect() # pylint: disable=attribute-defined-outside-init
        self.textrect.topleft = (X,Y)
        surface.blit(self.textobj, self.textrect)

    def on_render(self):
        """
        Näytön värit, fontti, teksti, kolikot, pelaajan hahmo ja ulosäynti

        Näytön virkistys
        """
        self._screen.fill((39, 39, 39))
        self.fontti = pygame.font.SysFont(None, 26) # pylint: disable=attribute-defined-outside-init
        self.fontti2 = pygame.font.SysFont(None, 30) # pylint: disable=attribute-defined-outside-init
        self.fontti3 = pygame.font.SysFont(None, 32) # pylint: disable=attribute-defined-outside-init
        pygame.draw.rect(self._screen, (165, 42, 42), self.exit)
        pygame.draw.rect(self._screen, (0, 205, 205), self.restart)
        self.end_page_text("Congratiulations, you made it!", self.fontti2, (0, 0, 0), self._screen, 180, 22) # pylint: disable=line-too-long
        self.end_page_text("Congratiulations, you made it!", self.fontti2, (34,139,34), self._screen, 178, 20) # pylint: disable=line-too-long
        self.end_page_text("Your time was:  " + f'{game_loop.GameLoop.Player_time:.2f}'+ " seconds", self.fontti, (255, 255, 255), self._screen, 215, 60) # pylint: disable=line-too-long
        self.end_page_text("Your total coins are:  " + str(game_loop.GameLoop.sum_coin), self.fontti, (205, 173, 0), self._screen, 215, 90) # pylint: disable=line-too-long
        self.end_page_text('EXIT', self.fontti, (0, 0, 0), self._screen, 300, 197)
        self.end_page_text('RESTART', self.fontti, (0, 0, 0), self._screen, 282, 237)
        pygame.display.update()

    def on_button(self):
        """
        Funktio määrittää hiiren painalluksen toiminnon
        Exit- sekä Restart-painikkeiden kohdalla

        self.exit = Exit painike
        self.restart = Restart-painike
        """
        mx, my = pygame.mouse.get_pos() # pylint: disable=invalid-name
        self.exit = pygame.Rect(245, 190, 150, 30) # pylint: disable=attribute-defined-outside-init
        self.restart = pygame.Rect(245, 230, 150, 30) # pylint: disable=attribute-defined-outside-init

        if self.exit.collidepoint((mx, my)):
            if self.click3:
                pygame.quit() # pylint: disable=no-member
                sys.exit()

        self._restart = game_loop.GameLoop() # pylint: disable=attribute-defined-outside-init
        if self.restart.collidepoint((mx, my)):
            if self.click3:
                self._restart.on_execute()

    def events(self):
        """
        Events; poistuminen ruksilla tai ESC-painikkeella
        """
        self.click3 = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # pylint: disable=no-member
                pygame.quit() # pylint: disable=no-member
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN: # pylint: disable=no-member
                if event.button == 1:
                    self.click3 = True

            if event.type == pygame.KEYDOWN: # pylint: disable=no-member
                if event.key == pygame.K_ESCAPE: # pylint: disable=no-member
                    pygame.quit() # pylint: disable=no-member
                    sys.exit()


    def end_page(self):
        """
        Funktio kutsuu aiempia funktioita jotta lopetussivun
        saa toimimaan
        """
        if self._on_init() is False:
            self._running = False

        while self._running:
            EndClock.tick(60)
            self.on_button()
            self.on_render()
            self.events()
