import pygame
walls = []

class Wall(object):
    def __init__(self, pos):
        walls.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 16, 16)

level = [
        "HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH",
        "HHH   H   H           H                H",
        "H   H   H HHHHHH H HH   HHHHHHHHHHHHHH H",
        "HH HHHHH       H  H H H H   H       H  H",
        "H   H        HHHH H H HHH H H HHHHH H HH",
        "H HHH  HHHH       H       H H H   H H  H",
        "H   H   H H H   HHHHH   HHHHH H H H HH H",
        "HH  H H   H   HHH     H     H H H H H  H",
        "H   HHH HHH   H H HHH H  H  H H H H H HH",
        "H       H     H H  H  H     H H H H H  H",
        "HHH H H   HHHHH HH H H   HH H H HHH HH H",
        "H H   H  HH        H  HH H  H H     H  H",
        "H H   HHHH   HHH HHHH  H  H H HHHHHHH HH",
        "H HH  H    H  H  H   HHH HH H          H",
        "H H      HHHH H HHHH     H  HHHHHHHHHHHH",
        "H   H    H  HHH    H   H H             H",
        "H    HHHHH      HH   HHH H HHH  HHHH   H",
        "H    H       HHHH        HHHHHH    HH  H",
        "H H HH  HHH  H H  HHHHHHH     H     H  H",
        "H HH    H    H HHHH  H    H  HHHHHH H  H",
        "H H  HHH   HH          H  HHHH    H H  H",
        "H   H HH  H   HHHHHHH HHH       H H H  H",
        "H H H H  HH   H     H H H    HHHH H H  H",
        "H    HH H HHH   HHHHH   H   H     H H  H",
        "HH HHH        HH     H  HH   HHH H  H  H",
        "H  H    H HH HH  HHH  HH HHHHH H H H   H",
        "H   HHH H H HH      H H     HH   H     H",
        "H     HHH H  HHHHHH H HHHHH   H  HH H  H",
        "H HH     HH         H       H  E   H   H",
        "HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH",
    ]
