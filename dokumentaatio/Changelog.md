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

## Viikko 5

* Peliin on lisätty lopetussivu, jossa tulisi näkyä pelin valmistuttua:
    * Kerätyt kolikot
    * Pelattu aika
    * **Exit**-painike
    * **Restart**-painike
* Lopetussivulta olisi ajatus pystyä käynnistämään peli uudelleen mutta se on vielä vaiheessa
* Korjaillut pylintin huomauttamia kohtia, muutamilla epäselvyyksillä
* Pelissä on nyt kolikoita joita pelaaja pystyy keräämään, niiden sijainti saattaa muuttua

## Viikko 6

* Pelin lopetussivulle on nyt lisätty:
    * Kerättyjen kolikoiden summa
    * Pelattu aika
    * **Exit**-painike
* Docstring-dokumentaatio aloitettu
* Lisäsin muutaman testin testikattavuutta varten
* Korjaillut pylintiä
* **Restart**-painike lisätty mutta ei vielä täysin toiminnassa, jokin bugi tällä hetkellä
* Muutellut joidenkin kolikoiden sijainteja
