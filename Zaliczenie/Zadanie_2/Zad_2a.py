#!/usr/bin/python
# Pamiętać należy aby w terminalu mieć zainstalowane odpowiednie biblioteki oraz odpalać przez polecenie "python Zad_2a.py"
# Importujemy potrzbne biblioteki
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# tworzymy zbiór rozkłądu normalnego i zapisujemy go do postaci pandas data frame
# parametry to:
#  środek:0 odchylenie standardowe: 10, liczebność: 70
print("Generowany jest zbiór danych o rozkładzie normalnym z parametrami, środek: 0 odchylenie standardowe: 10 liczebność: 70")
df = pd.DataFrame(np.random.normal(0,10,70))
df.columns = ['wartość']
df.head()
print("Wygenerowany rozkład: ")
print(df)
# Zapis do pliku .csv
df.to_csv('/home/studentb10/Sprawozdanie_Dawid_Ewa/Zadanie_2/plik_a.csv')
# Odczyt pliku
pd.read_csv('/home/studentb10/Sprawozdanie_Dawid_Ewa/Zadanie_2/plik_a.csv') 

# Sprawdzenie graficzne czy prezentowany rozkład jest rozkładem normalnym za pomocą biblioteki seaborn
print("Poniżej następuje próba generacji wykresu lecz możliwość ta jest ograniczona i pokazywany jest tylko komunikat, który należy pominąć właściwy wykres znajduje się w sprawozdaniu.")
print(" ")
sns.set(rc={"figure.figsize": (8, 4)}); np.random.seed(0)
a = sns.distplot(df)
plt.show()
print(" ")
print("Sprawdzenie czy wygenerowany rozkład jest faktycznie rozkładem normalnym")
print(" ")

# Wybór odpowiednich testów oraz ich użycie 

#Test D’Agostino–Pearson
print("Test D’Agostino–Pearson")
from scipy.stats import normaltest
stats, p = normaltest(df)
print(stats, p)
if p > 0.05:
    print ("Wynik: Rozkład wygląda na normalny")
else:
    print("Wynik: Rozkład nie jest normalny")
print(" ")

# Test Shapiro-Wilk
print("Test Shapiro-Wilk")
from scipy.stats import shapiro
stats, p = shapiro(df)
print(stats,p)
if p > 0.05:
    print ("Wynik: Rozkład wygląda na normalny")
else:
    print("Wynik: Rozkład nie jest normalny")
print(" ")
print("Koniec Zadania_2a")

