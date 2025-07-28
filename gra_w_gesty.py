import random

cykl_zwyciestw = {
    "Ślimak" : "Wąż",
    "Wąż" : "Żaba",
    "Żaba" : "Ślimak"
}

print("""
\033[34mZasady:\033[0m

        [ Żaba ]             Żaba \033[34m(- :)=\033[0m pokonuje Ślimaka \033[34m@-''\033[0m
      /         ↑            Ślimak \033[34m@-''\033[0m pokonuje Węża \033[34m>>:>~\033[0m
     ↓           \\           Wąż \033[34m>>:>~\033[0m pokonuje Żabę \033[34m(- :)=\033[0m
 [ Ślimak ] --> [ Wąż]
""")

wybor_komputera = random.choice(list(cykl_zwyciestw.keys()))

wybor_gracza = (input("""
Wprowadź nazwę swojego wyboru:
    \033[34mŚlimak\033[0m, \033[34mWąż\033[0m lub \033[34mŻaba\033[0m
"""))

print("\n\033[34mWybór Twojego przeciwnika to:\033[0m", [wybor_komputera])
print("\033[34mTwój wybór to:\033[0m", [wybor_gracza])
print("\nRezultatem tego spotkania jest:")

if (wybor_gracza == wybor_komputera):
    print("\033[34mRemis!\033[0m")
elif (cykl_zwyciestw[wybor_gracza] == wybor_komputera):
    print("\033[34mWygrana!\033[0m")
else:
    print("\033[34mPrzegrana!\033[0m")
