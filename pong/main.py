import pgzrun
from pgzero.builtins import keyboard
from paletka import *
from pilka import *
from stale import WIDTH
from wyniki import TablicaWynikow

paletka1 = Paletka('paletka.png', (50, 100))
paletka2 = Paletka('paletka.png', (WIDTH-50, 100))
pileczka = Pilka('pilka.png', (100, 120))
wyniki = TablicaWynikow()

def update():
    if keyboard.w:
        paletka1.ruch_gora()
    elif keyboard.s:
        paletka1.ruch_dol()
    if keyboard.up:
        paletka2.ruch_gora()
    elif keyboard.down:
        paletka2.ruch_dol()

    pileczka.ruch(paletka1, paletka2)
    wyniki.liczymy_punkty(pileczka)

def draw():
    screen.clear()
    paletka1.draw()
    paletka2.draw()
    pileczka.draw()
    screen.draw.text(f'{wyniki.punkty_paletka1} : {wyniki.punkty_paletka2}', (300, 100), fontsize = 30)

pgzrun.go()
