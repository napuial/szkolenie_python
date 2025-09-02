# Importy bibliotek
import folium
from streamlit_folium import st_folium
import streamlit as st
import requests
import pandas as pd
# folium – biblioteka do rysowania interaktywnych map (korzysta z Leaflet.js)
# streamlit_folium – pozwala wyświetlić mapę folium w aplikacji Streamlit i odczytywać kliknięcia użytkownika
# streamlit – framework do budowania prostych aplikacji webowych w Pythonie
# requests – do wysyłania zapytań HTTP (pobieranie danych z API)
# pandas – do przetwarzania danych w tabelach (DataFrame)

# Adres API
API_URL = "https://api.open-meteo.com/v1/forecast"
# publiczne API Open-Meteo – zwraca warunki pogodowe (m.in. temperaturę, wiatr, wilgotność)

# Nagłówki aplikacji
st.write("# Informacje pogodowe na świecie")
st.write("Wybierz interesujące Cię miejsce")

# Tworzenie mapy, Folium
map = folium.Map(tiles="CartoDB.Voyager")
# folium.Map() – tworzy mapę interaktywną
# tiles="CartoDB.Voyager" – ustawia styl mapy (ładny, jasny)

# Wyświetlenie mapy w Streamlit i obsługa kliknięcia
map_state = st_folium(map, width=725)
# st_folium() wyświetla mapę w aplikacji Streamlit
# zwraca słownik map_state, który zawiera m.in. współrzędne kliknięcia (map_state["last_clicked"])

# Sprawdzenie, czy użytkownik kliknął mapę
if map_state["last_clicked"]:
    latitude = map_state["last_clicked"]["lat"]
    longitude = map_state["last_clicked"]["lng"]
# jeżeli kliknięto mapę, zapisuje współrzędne klikniętego punktu (latitude, longitude)

# Przygotowanie zapytania do API
    querystring = {"latitude":latitude,
                   "longitude":longitude,
                   "hourly":"temperature_2m,wind_speed_10m,relative_humidity_2m"}
# zapytanie o:
#               temperature_2m – temperatura na wysokości 2m
#               wind_speed_10m – prędkość wiatru na 10m
#               relative_humidity_2m – wilgotność względna na 2m

# Pobranie danych pogodowych
    response = requests.get(API_URL, params=querystring)
    weather = response.json()
# wysyła żądanie GET do API z parametrami (params) i zwraca odpowiedź jako JSON

# Zamiana na DataFrame
    weather_df = pd.DataFrame(weather["hourly"])
# dane z klucza hourly w JSON-ie są przekształcane w tabelę Pandas

# Wykres liniowy temperatury w czasie
    st.line_chart(weather_df[["time", "temperature_2m"]],
                x = "time",
                y = "temperature_2m")
#  oś X to czas (x = "time")
#  oś Y to temperatura (y = "temperature_2m")

# Wyświetlenie tabeli z danymi
    st.write(weather_df)
