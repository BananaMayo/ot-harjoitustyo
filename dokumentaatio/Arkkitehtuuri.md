# Arkkitehtuurikuvaus
## Rakenne

Ohjelman päivitetty rakenne: (viimeinen sivu lisättynä)

![image](https://user-images.githubusercontent.com/101586122/165270406-3c6a299f-b02d-4918-9297-ac4b5deedae6.png)

## Pelin MazeGame käyttöliittymä

* Aloitussivu
* Pelinäkymä
* Lopetussivu

Käyttöliittymä sisältää kolme erikseen rakennettua luokkaa. Luokista siirrytään seuraavaan järjestyksessä.
Ensin aloitussivu, sitten pelinkämyä ja lopuksi lopetussivu. Lopullisessa versiossa olisi tarkoitus pystyä
käynnistämään peli uudelleen lopetussivulta.

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
