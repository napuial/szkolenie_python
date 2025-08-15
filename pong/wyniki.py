from pilka import Pilka
from stale import *

class TablicaWynikow:
    def __init__(self):
        self.punkty_paletka1 = 0
        self.punkty_paletka2 = 0

    def liczymy_punkty(self, pilka: Pilka):
        if pilka.right >= WIDTH:
            self.punkty_paletka1 += 1
            pilka.x, pilka.y = WIDTH // 2, HEIGHT // 2

        if pilka.left <= 0:
            self.punkty_paletka2 += 1
            pilka.x, pilka.y = WIDTH // 2, HEIGHT // 2
