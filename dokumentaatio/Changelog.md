# Changelog

## Viikko 3

* Peliä varten on tehty alustava pohja
  - Sisältää aloitussivun
  - Labyrinttipelin (Game1) jossa pelaajan hahmo (pinkki) sekä uloskäynti (lila)
  - Lopetussivuston koodipohja on lisätty mutta vielä vaiheessa
* Käyttäjä näkee aloitussivun
* Käyttäjä pystyy navigoimaan itsensä peliin painamalla pelin painiketta
* Käyttäjä pystyy pelaamaan labyrintti peliä
* Testattu että pelaajan sijainti täsmää

## Viikko 4

* Peli on jaettu tiedostoihi jotka sisältävät luokkia
* Aloitussivun tiedosto kutsuu näitä luokkia
  - Pelillä on toimiva aloitussivu
  - Labyrinttipeli toimii
 * Pelin pystyy käynnistämään `poetry run invoke start` -komennolla
 * Testin saa suoritettua `poetry run invoke test` -komennolla
 * Testikattavuus `poetry run invoke coverage-report` -komennolla
