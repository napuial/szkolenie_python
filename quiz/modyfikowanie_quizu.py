import csv

słownik_pytań = {}

#utworzenie słownika
with open("./quiz.csv", newline='', encoding='utf-8') as baza_pytań:
    wiersze = csv.DictReader(baza_pytań, delimiter=';')
    for wiersz in wiersze:
        pytanie = wiersz['pytanie']
        odpowiedzi = [wiersz['poprawna odpowiedź'], 
                      wiersz['błędna odpowiedź 1'], 
                      wiersz['błędna odpowiedź 2']]
        słownik_pytań[pytanie] = odpowiedzi

i = 1
#wydrukowanie słownika
for pytanie in słownik_pytań:
    print(f" {i}. {pytanie}")
    j= 1
    for odpowiedzi in słownik_pytań[pytanie]:
        print(f"   {j}) {odpowiedzi}")
        j += 1
    i += 1
    print()

print("""
Dostępne operacje:
      1. Wyświetl listę pytań
      2. Modyfikuj pytanie
      3. Dodaj pytanie
      4. Usuń pytanie
""")
