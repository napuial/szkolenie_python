from pgzero.builtins import Actor
from stale import HEIGHT

class Paletka(Actor):
    def __init__(self, obrazek, polozenie):
        super().__init__(obrazek, polozenie)

    def ruch_gora(self):
        if self.top > 0:
            self.y -= 5

    def ruch_dol(self):
        if self.bottom < HEIGHT:
            self.y += 5
