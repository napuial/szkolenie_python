import csv
import flet

CSV_FILE = "quiz.csv"

def main(page: flet.Page):

    page.title = "Quiz"
    
    def dodaj_pytanie(e):
        nowe_pytanie_str = nowe_pytanie.value
        nowe_pytanie_poprawna_odpowiedz_str = nowe_pytanie_poprawna_odpowiedz.value
        nowe_pytanie_bledna_odpowiedz_1_str = nowe_pytanie_bledna_odpowiedz_1.value
        nowe_pytanie_bledna_odpowiedz_2_str = nowe_pytanie_bledna_odpowiedz_2.value

        with open(CSV_FILE, mode="a", newline="", encoding="utf-8") as baza_pytan:
            writer = csv.writer(baza_pytan)
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

    def usun_pytanie(e):
        pytanie_do_usuniecia_str = pytanie_do_usuniecia.value
        with open(CSV_FILE, mode="r", newline="", encoding="utf-8") as baza_pytan:
            reader = csv.reader(baza_pytan)
            wiersze = list(reader)

        wyczyszczona_baza_pytan = [
            wiersz for wiersz in wiersze
            if wiersz and wiersz[0] != pytanie_do_usuniecia_str]

        with open(CSV_FILE, mode="w", newline="", encoding="utf-8") as baza_pytan:
            writer = csv.writer(baza_pytan)
            writer.writerows(wyczyszczona_baza_pytan)

        print("Wykonano operację: Usuń pytanie")

        pytanie_do_usuniecia.value = ""
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
    )

flet.app(main)
