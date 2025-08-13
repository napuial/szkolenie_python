import csv
import flet

CSV_FILE = "quiz.csv"

def main(page: flet.Page):

    page.title = "Quiz"
    page.scroll = "adaptive"
    
    slownik_pytan = {}
    lista_pytan = flet.Column()
    
    def dodaj_pytanie(e):
        nowe_pytanie_str = nowe_pytanie.value
        nowe_pytanie_poprawna_odpowiedz_str = nowe_pytanie_poprawna_odpowiedz.value
        nowe_pytanie_bledna_odpowiedz_1_str = nowe_pytanie_bledna_odpowiedz_1.value
        nowe_pytanie_bledna_odpowiedz_2_str = nowe_pytanie_bledna_odpowiedz_2.value

        with open(CSV_FILE, mode="a", newline="", encoding="utf-8") as baza_pytan:
            writer = csv.writer(baza_pytan, delimiter=';')
            writer.writerow([nowe_pytanie_str, 
                             nowe_pytanie_poprawna_odpowiedz_str, 
                             nowe_pytanie_bledna_odpowiedz_1_str, 
                             nowe_pytanie_bledna_odpowiedz_2_str])
            
        print("Wykonano operację: Dodaj pytanie")

        nowe_pytanie.value = ""
        nowe_pytanie_poprawna_odpowiedz.value = ""
        nowe_pytanie_bledna_odpowiedz_1.value = ""
        nowe_pytanie_bledna_odpowiedz_2.value = ""

        page.update()
        odswiez_liste()


    def usun_pytanie(e):
        pytanie_do_usuniecia_str = pytanie_do_usuniecia.value
        with open(CSV_FILE, mode="r", newline="", encoding="utf-8") as baza_pytan:
            reader = csv.reader(baza_pytan, delimiter=";")
            wiersze = list(reader)

        wyczyszczona_baza_pytan = [
            wiersz for wiersz in wiersze
            if wiersz and wiersz[0] != pytanie_do_usuniecia_str]

        with open(CSV_FILE, mode="w", newline="", encoding="utf-8") as baza_pytan:
            writer = csv.writer(baza_pytan, delimiter=";")
            writer.writerows(wyczyszczona_baza_pytan)

        print("Wykonano operację: Usuń pytanie")

        pytanie_do_usuniecia.value = ""
        page.update()
        odswiez_liste()

    def utworz_slownik_pytan():
        with open(CSV_FILE, newline='', encoding='utf-8') as baza_pytan:
            wiersze = csv.DictReader(baza_pytan, delimiter=';')
            for wiersz in wiersze:
                pytanie = wiersz['pytanie']
                odpowiedzi = [
                    wiersz['poprawna odpowiedź'],
                    wiersz['błędna odpowiedź 1'],
                    wiersz['błędna odpowiedź 2']]
                slownik_pytan[pytanie] = odpowiedzi
        return slownik_pytan

    def odswiez_liste(_=None):
        lista_pytan.controls.clear()
        slownik_pytan.clear()
        slownik_pytan.update(utworz_slownik_pytan())
        for pytanie in slownik_pytan.keys():
            przycisk_edycji_pytania = flet.FilledButton("Edytuj", on_click=edytuj_pytanie)
            przycisk_edycji_pytania.data = pytanie
            lista_pytan.controls.append(flet.Row([flet.Text(pytanie, expand=True), przycisk_edycji_pytania]))
        page.update()

    def edytuj_pytanie(event):
        pytanie = event.control.data
        odpowiedzi = slownik_pytan[pytanie]
        
        input_pytanie = flet.TextField(value=pytanie, label="Pytanie")
        input_odp1 = flet.TextField(value=odpowiedzi[0], label="Poprawna odpowiedź")
        input_odp2 = flet.TextField(value=odpowiedzi[1], label="Błędna odpowiedź 1")
        input_odp3 = flet.TextField(value=odpowiedzi[2], label="Błędna odpowiedź 2")

        def zapisz_slownik_do_pliku(e, stare_pytanie = pytanie):
            nowy_klucz = input_pytanie.value
            slownik_pytan.pop(stare_pytanie)
            slownik_pytan[nowy_klucz] = [input_odp1.value, input_odp2.value, input_odp3.value]
                
            with open(CSV_FILE, mode="w", newline='', encoding='utf-8') as baza_pytań:
                writer = csv.writer(baza_pytań, delimiter=';')
                writer.writerow(["pytanie", "poprawna odpowiedź", "błędna odpowiedź 1", "błędna odpowiedź 2"])
                for pytanie, odpowiedzi in slownik_pytan.items():
                    writer.writerow([pytanie] + odpowiedzi)
            print("Wykonano operację: Modyfikuj pytanie")
            odswiez_liste()
        
        przycisk_zapisz = flet.FilledButton("Zatwierdź operację - Modyfikuj Pytanie", on_click=zapisz_slownik_do_pliku)

        lista_pytan.controls.append(flet.Column([
            input_pytanie, input_odp1, input_odp2, input_odp3, przycisk_zapisz
        ]))
        page.update()

    operacja_dodaj_pytanie = flet.Text("Operacja: Dodaj pytanie")
    nowe_pytanie = flet.TextField(label="Treść pytania: ")
    nowe_pytanie_poprawna_odpowiedz = flet.TextField(label="Treść poprawnej odpowiedzi: ")
    nowe_pytanie_bledna_odpowiedz_1 = flet.TextField(label="Treść błędnej odpowiedzi 1: ")
    nowe_pytanie_bledna_odpowiedz_2 = flet.TextField(label="Treść błędnej odpowiedzi 2: ")
    przycisk_zatwierdzenia_operacji_dodaj_pytanie = flet.FilledButton("Zatwierdź operację - Dodaj pytanie",
                                 on_click=dodaj_pytanie)
    
    operacja_usun_pytanie = flet.Text("Operacja: Usuń pytanie")
    pytanie_do_usuniecia = flet.TextField(label="Pytanie do usunięcia: ")
    przycisk_zatwierdzenia_operacji_usun_pytanie = flet.FilledButton("Zatwierdź operację - Usuń pytanie",
                                 on_click=usun_pytanie)
    
    page.add(
        operacja_dodaj_pytanie,
        nowe_pytanie,
        nowe_pytanie_poprawna_odpowiedz,
        nowe_pytanie_bledna_odpowiedz_1,
        nowe_pytanie_bledna_odpowiedz_2,
        przycisk_zatwierdzenia_operacji_dodaj_pytanie,
        operacja_usun_pytanie,
        pytanie_do_usuniecia,
        przycisk_zatwierdzenia_operacji_usun_pytanie,
        flet.Text("Operacja: Modyfikuj pytanie"),
        lista_pytan
    )

    odswiez_liste()

flet.app(main)
