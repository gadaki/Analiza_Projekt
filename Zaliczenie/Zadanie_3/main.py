import dataparser

# Załadowanie danych z pliku. "data" jest listą zawierającą linie wczytanego pliku
data = dataparser.load_data_from_file("Dane_Zad_3.csv")
# Przetworzenie danych z pliku
items_ok, items_nok = dataparser.parse_data(data)
# Obliczanie opóźnienia i czasu postoju
dataparser.calc_delay_and_layover_time(items_ok)
# Zapis do pliku SQLite
dataparser.save_to_sqlite("result.sqlite3", items_ok)
# Zapis do pliku CSV
dataparser.save_to_csv("Not_ok.csv", items_nok)

# Wyświetlenie statystyk
print("Ilość danych: " + str(len(items_ok) + len(items_nok)))
print("Poprawny/Poprawiony zapis: " + str(len(items_ok)))
print("Błedny zapis: " + str(len(items_nok)))
