from random import randint

class Monopoli:
    def __init__(self, players:int):
        for p in range(1, players+1):
            self.p = Pelaaja(p)

    def noppa(self, pelaaja):
        numerot = (randint(1,6), randint(1,6))
        pelaaja.p.sijainti = sum(numerot)

class Pelaaja:
    def __init__ (self, pelaaja:int):
            self.pelaaja = pelaaja
            self.sijainti = 1

class Ruutu:
    def __init__(self, ruutu:int):
        for ruutu in range(1,41):
            self.ruutu = ruutu

    