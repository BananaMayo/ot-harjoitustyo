# Arkkitehtuurikuvaus
## Rakenne

**Ohjelman rakenne:**

![image](https://user-images.githubusercontent.com/101586122/165270406-3c6a299f-b02d-4918-9297-ac4b5deedae6.png)

## Pelin MazeGame käyttöliittymä

Käyttöliittymä sisältää kolme näkymää, jotka ovat:

* Aloitussivu
* Pelinäkymä
* Lopetussivu

Käyttöliittymä sisältää kolme erikseen rakennettua pääluokkaa, näiden lisäksi on sekä pelaaja- että tasoluokka joista pääluokat tarvitsevat tietoa. Luokista siirrytään järjestyksessä seuraavaan.
Ensin aloitussivu, sitten pelinkämyä ja lopuksi lopetussivu. Lopullisessa versiossa olisi tarkoitus pystyä
käynnistämään peli uudelleen lopetussivulta.

## Pelin sovelluslogiikka

- **Peli sisältää siis viisi luokkaa. Pelin aloitussivun muodostaa luokka [main_menu.py](https://github.com/BananaMayo/ot-harjoitustyo/blob/master/src/main_menu.py)-tiedostosta joka ohjaa peliin painettua sivun painiketta.** 

  Luokka sisältää useampia funktioita, muun muassa seuraavat:
  * `menu_text(self, text, font, color, surface, x, y)`
  * `on_render(self)`
  * `on_button(self)`
  * `main_menu(self)` Tämä funktio aktivoi edellä mainittuja funktioita

- **Pelinäkymä muodostuu luokan [game_loop.py](https://github.com/BananaMayo/ot-harjoitustyo/blob/master/src/game_loop.py) avulla. Päästyään uloskäynnille kutsuu tämä luokka lopetussivun luokkaa.**

  Funktiot pelinäkymän luokassa ovat mm.:
  * `on_render(self)`
  * `on_moving(self)` Tämä funktio määrittää liikkumisen
  * `on_execute(self)` Pääfunktio joka kutsuu edellämainittuja funktioita

- **Lopetussivulla on käytössä luokka [end_page.py](https://github.com/BananaMayo/ot-harjoitustyo/blob/master/src/end_page.py)-tiedostosta.** 

  Luokka sisältää useampia funktioita, muun muassa:
  * `on_render(self)` Tämän avulla aika että kolikot näkyvät pelaajalle
  * `on_button(self)` Tämän avulla Exit- ja Restart-painike toimii
  * `end_page(self)` Pääfunktio joka kutsuu edellämainittuja funktioita

  
- **Pelaajan funktiot ovat tallennettuna luokassa Player, joka löytyy [player.py](https://github.com/BananaMayo/ot-harjoitustyo/blob/master/src/player.py)-tiedostosta**
  * `move(self, dx, dy)` Funktio on osa pelaajan liikkumista
  * `advance_single_axis(self, dx, dy)` Funktio on osa pelaajan liikkumista
 
- **Tason ulkonäkö ja muoto on tallennettuna luokassa Wall joka löytyy tiedostosta [levels.py](https://github.com/BananaMayo/ot-harjoitustyo/blob/master/src/levels.py)**
  * `__init__(self, pos)`
  * Muuttuja `level` pitää huolta tason ulkonäöstä

## Sekvenssikaavio

![image](https://user-images.githubusercontent.com/101586122/166227286-fae9a844-ac13-488c-8c25-08336690238e.png)


## Pelin päätoiminnallisuudet

### Aloitussivu
Pelin ensinäkymä on aloitussivu. Aloitussivu sisältää tekstiä ja pelin painikkeen 'MazeGame', se hyödyntää tiedostoa 
[main_menu.py](https://github.com/BananaMayo/ot-harjoitustyo/blob/master/src/main_menu.py) ja sen sisältämää 
luokkaa `Main`. Aloitussivulta pääsee navigoimaan itsensä peliin painamalla painiketta.

### Pelinäkymä
Pelinäkymä tarjoaa pelaajalleen labyrintin, hahmon jota liikuttaa, kolikoita sekä uloskäynnin. Kerättyjen kolikoiden
summa ja aika näkyy pelatessa. Peli loppuu pelaajan löydettyä reitin uloskäynnille. Pelinäkymässä hyödynnän [game_loop.py](https://github.com/BananaMayo/ot-harjoitustyo/blob/master/src/game_loop.py) tiedostoa, ja sen sisältämää luokkaa `GameLoop`. Tämän lisäksi käytän tiedostoja [player.py](https://github.com/BananaMayo/ot-harjoitustyo/blob/master/src/player.py) ja [levels.py](https://github.com/BananaMayo/ot-harjoitustyo/blob/master/src/levels.py) tässä toiminnallisuudessa.

### Lopetussivu
Pelaajan löydettyä uloskäynnin saa hän näkyvilleen lopetussivun. Lopetussivu näyttää pelaajalleen kolikoiden summan ja pelatun ajan. Sivulla on myös Exit-painike jonka avulla pelistä pääsee pois. Lopetussivu käyttää luokkaa 
`End` tiedostosta [end_page.py](https://github.com/BananaMayo/ot-harjoitustyo/blob/master/src/end_page.py).
