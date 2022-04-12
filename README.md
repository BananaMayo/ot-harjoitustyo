# MazeGame

MazeGame on pygamella toteutettu hasuka pieni peli. Pelissä on labyrintti jossa tavoitteena on päästä ulos, löytämällä uloskäynti.

## Python-versiosta
Sovellus on toiminnallisuudeltaan testattu Python-versiolla `3.8`

## Dokumentaatio
* [Vaatimusmäärittely](https://github.com/BananaMayo/ot-harjoitustyo/blob/master/dokumentaatio/Vaatimusm%C3%A4%C3%A4rittely.md#grejor)
* [Tuntikirjanpito](https://github.com/BananaMayo/ot-harjoitustyo/blob/master/dokumentaatio/Tuntikirjanpito.md#mera-grejor)
* [Changelog](https://github.com/BananaMayo/ot-harjoitustyo/blob/master/dokumentaatio/Changelog.md)


## Asennus
1. Riippuvuuksien asennus komennolla:
```
$ poetry install
```
2. Sovelluksen käynnistäminen komennolla:
```
$ poetry run invoke start
```

## Toiminnot komentorivillä
### Ohjelman suorittaminen
Ohjelman pystyy suorittamaan komennolla:
```
$ poetry run invoke start
```
### Testaaminen
Ohjelman pystyy testaamaan komennolla:
```
$ poetry run invoke test
```
### Testikattavuus
Testikattavuuden generointi komennolla:
```
$ poetry run invoke coverage-report
```
Raportti löytyy hakemistosta ***htmlcov***

### Pylint
Tiedoston .pylintrc määrittelemät tarkistukset voi suorittaa komennolla:
```
$ poetry run invoke lint
```
