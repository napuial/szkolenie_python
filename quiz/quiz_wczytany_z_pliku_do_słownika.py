import random
import csv

słownik_pytań = {}
zdobyte_punkty = 0

with open("./quiz.csv", newline='', encoding='utf-8') as baza_pytań:
    wiersze = csv.DictReader(baza_pytań, delimiter=';')
    for wiersz in wiersze:
        pytanie = wiersz['pytanie']
        odpowiedzi = [(wiersz['poprawna odpowiedź'], True), 
                      (wiersz['błędna odpowiedź 1'], False), 
                      (wiersz['błędna odpowiedź 2'], False)]
        random.shuffle(odpowiedzi)
        słownik_pytań[pytanie] = odpowiedzi

pytania = list(słownik_pytań.keys())
random.shuffle(pytania)

for pytanie in pytania:
    print(pytanie)
    i = 1
    for odpowiedz in słownik_pytań[pytanie]:
        print(f" {i}) {odpowiedz[0]}")
        i += 1
    user_input = int(input("Wskaż numer poprawnej odpowiedzi: "))
    if słownik_pytań[pytanie][user_input-1][1]:
        zdobyte_punkty +=1
    print()

print("Uzyskane punkty:", zdobyte_punkty)
