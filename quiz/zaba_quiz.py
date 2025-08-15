import turtle as t
import time

pytania = [
    {
        "pytanie": "Jak nazywa się największy gatunek żaby na świecie?",
        "odpowiedzi": ["Żaba goliat", "Żaba trawna", "Ropucha szara"],
        "poprawna": "Żaba goliat"
    },
    {
        "pytanie": "Jak żaby oddychają?",
        "odpowiedzi": ["Tylko przez skórę", "Tylko przez skrzela", "Przez płuca i skórę"],
        "poprawna": "Przez płuca i skórę"
    },
    {
        "pytanie": "Jakie środowisko jest typowe dla żab?",
        "odpowiedzi": ["Pustynie", "Lasy deszczowe i tereny wodne", "Arktyka"],
        "poprawna": "Lasy deszczowe i tereny wodne"
    }
]

screen = t.Screen()
screen.setup(width=1000, height=700)
screen.title("Quiz")

pen_naglowek = t.Turtle(visible=False)
pen_naglowek.penup()

pen_zaba = t.Turtle(visible=False)
pen_zaba.speed(0)
pen_zaba.penup()

pen_usta = t.Turtle(visible=False)
pen_usta.speed(0)
pen_usta.penup()

pen_pytania = t.Turtle(visible=False)
pen_pytania.penup()

index_aktualnego_pytania = 0
punkty = 0

def rysuj_napis():
    pen_naglowek.goto(-200, 250)
    pen_naglowek.color("darkgreen")
    pen_naglowek.write("QUIZ", font=("Arial", 60, "bold"))

def rysuj_zabe():
    x, y = 300, -100

    pen_zaba.penup()
    pen_zaba.goto(x, y - 100)
    pen_zaba.pendown()
    pen_zaba.color("limegreen")
    pen_zaba.begin_fill()
    pen_zaba.circle(100)
    pen_zaba.end_fill()

    for oko_x in [-50, 50]:
        pen_zaba.penup()
        pen_zaba.goto(x + oko_x, y + 60)
        pen_zaba.pendown()
        pen_zaba.color("white")
        pen_zaba.begin_fill()
        pen_zaba.circle(30)
        pen_zaba.end_fill()

        pen_zaba.penup()
        pen_zaba.goto(x + oko_x, y + 75)
        pen_zaba.pendown()
        pen_zaba.color("black")
        pen_zaba.begin_fill()
        pen_zaba.circle(15)
        pen_zaba.end_fill()

        pen_zaba.penup()
        pen_zaba.goto(x + oko_x + 5, y + 80)
        pen_zaba.pendown()
        pen_zaba.color("white")
        pen_zaba.begin_fill()
        pen_zaba.circle(5)
        pen_zaba.end_fill()

    for policzki_x in [-60, 60]:
        pen_zaba.penup()
        pen_zaba.goto(x + policzki_x, y + 20)
        pen_zaba.pendown()
        pen_zaba.color("pink")
        pen_zaba.begin_fill()
        pen_zaba.circle(15)
        pen_zaba.end_fill()

    rysuj_usta("neutral")

def rysuj_usta(emocja="neutralna"):
    pen_usta.clear()
    x, y = 300, -120

    if emocja == "radosna":
        pen_usta.penup()
        pen_usta.goto(x - 40, y + 20)
        pen_usta.setheading(-60)
        pen_usta.pendown()
        pen_usta.width(4)
        pen_usta.color("black")
        pen_usta.circle(50, 120)
    elif emocja == "smutna":
        pen_usta.penup()
        pen_usta.goto(x - 40, y - 5)
        pen_usta.setheading(60)
        pen_usta.pendown()
        pen_usta.width(4)
        pen_usta.color("black")
        pen_usta.circle(-50, 120)
    else:
        pen_usta.penup()
        pen_usta.goto(x - 40, y + 10)
        pen_usta.setheading(0)
        pen_usta.pendown()
        pen_usta.width(4)
        pen_usta.color("black")
        pen_usta.forward(80)

    pen_usta.width(1)

aktualne_pytanie = None

def pokaz_pytanie():
    pen_pytania.clear()
    aktualne_pytanie = pytania[index_aktualnego_pytania]
    pen_pytania.goto(-400, 100)
    pen_pytania.write(aktualne_pytanie["pytanie"], font=("Arial", 24, "normal"))

    for i in range(len(aktualne_pytanie["odpowiedzi"])):
        wariant_odpowiedzi = aktualne_pytanie["odpowiedzi"][i]
        pen_pytania.goto(-400, 50 - i*40)
        pen_pytania.write(f"{i+1}. {wariant_odpowiedzi}", font=("Arial", 18, "normal"))

def wybierz_odpowiedz(index):
    global index_aktualnego_pytania
    aktualne_pytanie = pytania[index_aktualnego_pytania]

    wybrana = aktualne_pytanie["odpowiedzi"][index]
    if wybrana == aktualne_pytanie["poprawna"]:
        global punkty 
        punkty += 1
        rysuj_usta("radosna")
    else:
        rysuj_usta("smutna")
    
    screen.update()
    time.sleep(1)
    rysuj_usta("neutralna")
    index_aktualnego_pytania += 1
    if index_aktualnego_pytania >= len(pytania):
        pen_pytania.clear()
        pen_zaba.clear()
        pen_usta.clear()
        pen_pytania.goto(-200, 50)
        pen_pytania.write("KONIEC QUIZU!", font=("Arial", 36, "bold"))
        pen_pytania.goto(-180, -50)
        pen_pytania.write(f"Wynik: {punkty}/{len(pytania)}. Gratulacje!", font=("Arial", 24, "normal"))
        time.sleep(4)
        screen.bye()
    else:
        pokaz_pytanie()


def odpowiedz_1():
    wybierz_odpowiedz(0)

def odpowiedz_2():
    wybierz_odpowiedz(1)

def odpowiedz_3():
    wybierz_odpowiedz(2)

screen.listen()
screen.onkey(odpowiedz_1, "1")
screen.onkey(odpowiedz_2, "2")
screen.onkey(odpowiedz_3, "3")

rysuj_napis()
rysuj_zabe()
pokaz_pytanie()

screen.mainloop()
