# Pelin testausdokumentti

Peliä on testattu unittestilla

## Aloitussivun testaus:
- Aloitussivun testauksessa on käytössä tiedosto [main_menu_test.py] 
    * Testitedostossa on tällä hetkellä yksi testi `test_main_to_game(self)` joka testaa pääsivulta siirtymistä peliin 
    painikkeen kautta.

## Pelinäkymän testaus
- Pelinäkymää testaa tiedosto [game_loop_test.py] 
    * Testi `test_aloituspaikka(self)` testaa pelaajaan aloituspaikan ja että se täsmää annettujen tietojen kanssa
    * Testi `test_raha(self)` testaa että jokaisesta kerätystä kolikosta summa kasvaa kymmenellä.
    * Testi `test_ending(self)` testaa että uloskänniltä siirrytään lopetussivulle
