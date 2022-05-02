# Käyttöohje 

Projektin saa ladattua sivun **RELEASEN** kautta. Lähdekoodi löytyy `.zip` muodossa

## Käynnistykseen liittyvät ohjeet

Riippuvuuksien asennus saadaan aikaan komennolla:
```
$ poetry install
```
Pelin käynnistäminen toimii komennolla:
```
$ poetry run invoke start
```

## Pelin pääsivu
Pelin käynnistyttyä pelaaja saa näkyville pääsivun

![image](https://user-images.githubusercontent.com/101586122/166220946-a2b9d2e4-11cb-45c1-92ac-27c98a17f8bd.png)

Pääsivulta pääsee käynnistämään pelin painamalla 'MazeGame'-painiketta.

## Pelinäkymä
Pelinäkymä on seuraavanlainen:

![image](https://user-images.githubusercontent.com/101586122/166221321-33bdae02-e024-4350-a727-7e7f4639a9f6.png)

Pelaaja pystyy liikkumaan nuolinäppäimillä. Kolikkoja pystyy keräämään ja kolikoiden määrä näkyy vasemmassa
yläkulmassa. Maali on merkattua liilalla värillä, pelaaja itse on vaaleanpunainen.

## Lopetussivu
Tämä sivu on keskeneräinen:

![image](https://user-images.githubusercontent.com/101586122/166221906-59a1f2f2-6c9d-4dfe-b2d9-307b7740113a.png)

Lopetussivulla tulisi valmistuttua näkyä kolikoiden määrä, pelaajan aika,
Restart-painike ja Exit-painike.
