#SEKCJA PYTAŃ I ODPOWIEDZI

pytanie_1 = """\033[32m
    1. Jak nazywa się największy gatunek żaby na świecie?
     a) Żaba goliat
     b) Żaba trawna
     c) Ropucha szara
    \033[0m"""
poprawna_odpowiedz_1 = "a"

pytanie_2 = """\033[32m
    2. Jak żaby oddychają?
     a) Tylko przez skrzela
     b) Przez płuca i skórę
     c) Tylko przez skórę
    \033[0m"""
poprawna_odpowiedz_2 = "b"

pytanie_3 = """\033[32m
    3. Jakie środowisko jest typowe dla żab?
     a) Pustynie
     b) Lasy deszczowe i tereny wodne
     c) Arktyka
    \033[0m"""
poprawna_odpowiedz_3 = "b"

pytanie_4 = """\033[32m
    4. Co jest głównym pożywieniem dorosłych żab?
     a) Nasiona
     b) Owady
     c) Glony
    \033[0m"""
poprawna_odpowiedz_4 = "b"

pytanie_5 = """\033[32m
    5. Jak nazywa się młoda postać żaby?
     a) Larwa
     b) Kijanka
     c) Pisklę
    \033[0m"""
poprawna_odpowiedz_5 = "b"

pytanie_6 = """\033[32m
    6. Jaką cechą odznacza się skóra żab?
     a) Jest sucha i szorstka
     b) Jest gładka i wilgotna
     c) Jest pokryta łuskami
    \033[0m"""
poprawna_odpowiedz_6 = "b"

pytanie_7 = """\033[32m
    7. Jak żaby komunikują się między sobą?
     a) Poprzez śpiew lub rechot
     b) Poprzez wydzielanie feromonów
     c) Poprzez gesty
    \033[0m"""
poprawna_odpowiedz_7 = "a"

pytanie_8 = """\033[32m
    8. Jak długo żyją żaby w naturalnym środowisku?
     a) Zazwyczaj 1-2 lata
     b) Około 5-10 lat
     c) Zawsze ponad 20 lat
    \033[0m"""
poprawna_odpowiedz_8 = "b"

pytanie_9 = """\033[32m
    9. Który kontynent NIE jest zamieszkany przez żaby?
     a) Australia
     b) Antarktyda
     c) Ameryka Południowa
    \033[0m"""
poprawna_odpowiedz_9 = "b"

pytanie_10 = """\033[32m
    10. Jaką rolę odgrywają żaby w ekosystemie?
     a) Są tylko drapieżnikami
     b) Są zarówno drapieżnikami, jak i ofiarami
     c) Nie mają znaczenia w łańcuchu pokarmowym
    \033[0m"""
poprawna_odpowiedz_10 = "b"

#SEKCJA KOMUNIKATÓW

komunikat_wprowadz_odpowiedz = "Wybierz literę (a, b lub c), która odpowiada poprawnej odpowiedzi:"
komunikat_poprawna_odpowiedz = "Brawo! To poprawna odpowiedź!"
komunikat_zla_odpowiedz = "Niestety wskazana odpowiedź nie jest poprawna."

#SEKCJA POWITANIA UŻYTKOWNIKA

print("""
Hej!

    \033[32m@\033[0m...\033[32m@\033[0m  
   \033[32m(\033[0m• - •\033[32m)\033[0m  
   \033[32m(\033[0m>\033[32m ♡ \033[0m<\033[32m)\033[0m   
   \033[32m^^   ^^\033[0m

Wiesz dużo o żabach?
Sprawdź swoją wiedzę w quizie!""")

#SEKCJA LOGIKI QUIZU
suma_zdobytych_punktow = 0

print(pytanie_1, komunikat_wprowadz_odpowiedz, sep="\n")
if (poprawna_odpowiedz_1 == input().lower()):
  print(komunikat_poprawna_odpowiedz)
  suma_zdobytych_punktow += 1
else:
  print(komunikat_zla_odpowiedz)
  suma_zdobytych_punktow -= 0.5

print(pytanie_2, komunikat_wprowadz_odpowiedz, sep="\n")
if (poprawna_odpowiedz_2 == input().lower()):
  print(komunikat_poprawna_odpowiedz)
  suma_zdobytych_punktow += 1
else:
  print(komunikat_zla_odpowiedz)
  suma_zdobytych_punktow -= 0.5

print(pytanie_3, komunikat_wprowadz_odpowiedz, sep="\n")
if (poprawna_odpowiedz_3 == input().lower()):
  print(komunikat_poprawna_odpowiedz)
  suma_zdobytych_punktow += 1
else:
  print(komunikat_zla_odpowiedz)
  suma_zdobytych_punktow -= 0.5

print(pytanie_4, komunikat_wprowadz_odpowiedz, sep="\n")
if (poprawna_odpowiedz_4 == input().lower()):
  print(komunikat_poprawna_odpowiedz)
  suma_zdobytych_punktow += 1
else:
  print(komunikat_zla_odpowiedz)
  suma_zdobytych_punktow -= 0.5

print(pytanie_5, komunikat_wprowadz_odpowiedz, sep="\n")
if (poprawna_odpowiedz_5 == input().lower()):
  print(komunikat_poprawna_odpowiedz)
  suma_zdobytych_punktow += 1
else:
  print(komunikat_zla_odpowiedz)
  suma_zdobytych_punktow -= 0.5

print(pytanie_6, komunikat_wprowadz_odpowiedz, sep="\n")
if (poprawna_odpowiedz_6 == input().lower()):
  print(komunikat_poprawna_odpowiedz)
  suma_zdobytych_punktow += 1
else:
  print(komunikat_zla_odpowiedz)
  suma_zdobytych_punktow -= 0.5

print(pytanie_7, komunikat_wprowadz_odpowiedz, sep="\n")
if (poprawna_odpowiedz_7 == input().lower()):
  print(komunikat_poprawna_odpowiedz)
  suma_zdobytych_punktow += 1
else:
  print(komunikat_zla_odpowiedz)
  suma_zdobytych_punktow -= 0.5

print(pytanie_8, komunikat_wprowadz_odpowiedz, sep="\n")
if (poprawna_odpowiedz_8 == input().lower()):
  print(komunikat_poprawna_odpowiedz)
  suma_zdobytych_punktow += 1
else:
  print(komunikat_zla_odpowiedz)
  suma_zdobytych_punktow -= 0.5

print(pytanie_9, komunikat_wprowadz_odpowiedz, sep="\n")
if (poprawna_odpowiedz_9 == input().lower()):
  print(komunikat_poprawna_odpowiedz)
  suma_zdobytych_punktow += 1
else:
  print(komunikat_zla_odpowiedz)
  suma_zdobytych_punktow -= 0.5

print(pytanie_10, komunikat_wprowadz_odpowiedz, sep="\n")
if (poprawna_odpowiedz_10 == input().lower()):
  print(komunikat_poprawna_odpowiedz)
  suma_zdobytych_punktow += 1
else:
  print(komunikat_zla_odpowiedz)
  suma_zdobytych_punktow -= 0.5

print("\nTwój wynik to\033[32m", suma_zdobytych_punktow,
      "/ 10 punktów\033[0m!")
