from pgzero.builtins import Actor
from stale import HEIGHT

class Pilka(Actor):
    def __init__(self, obrazek, polozenie, size: int = 30):
        super().__init__(obrazek, polozenie)
        self.ruch_x = 3
        self.ruch_y = 3
        self.width = size
        self.height = size

    def ruch(self, obiekt_kolizyjny1, obiekt_kolizyjny2):
        self.x += self.ruch_x
        self.y += self.ruch_y

        if self.colliderect(obiekt_kolizyjny1) or self.colliderect(obiekt_kolizyjny2):
            self.ruch_x *= -1

        if self.top <= 0 or self.bottom >= HEIGHT:
            self.ruch_y *= -1
