print("Zadanie_2b") 
print("Do utworzenia szeregu czasowego posłużono się średnimi cenami w miesiącu ropy naftowej na giełdzie za rok 2021")
print("Dane są to ceny średnie ceny baryłki ropy za dany miesiąc dane odczytano ze strony: https://pl.investing.com/commodities/brent-oil-historical-data")
#Pobieramy zestaw niezbędnych pakietów
# Pamiętać należy aby w terminalu mieć zainstalowane odpowiednie biblioteki oraz odpalać przez polecenie "python Zad_2b.py"
#!/usr/bin/python
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
# Tworzymy dane za pomocą słownika
dict = {
    'Miesiąc': ['styczeń','luty','marzec','kwiecień','maj','czerwiec','lipiec','sierpień','wrzesień','październik','listopad','grudzień'],
    'Cena' : [55.88,66.13,63.54,67.25,69.32,75.13,76.33,72.99,78.52,84.38,70.57,77.78]}


# Przekształcamy oraz zapisujmy dane za pomocą dataframe do pliku z roszrzeniem.CSV
df = pd.DataFrame(dict)
df.to_csv('/home/studentb10/Sprawozdanie_Dawid_Ewa/Zadanie_2/plik_b.csv')
print("Dane prezentują się następująco:")
print(df)

# Oczyszczamy dane tak aby pozostały same wartości liczbowe w celu możliwości ich dalszej analizy
vals = (df['Cena'].tolist())
print("Oczyszczona lista tylko z cenami:",vals)

# Analizujemy dane w tym celu pobieramy odpowiednie pakiety
import scipy
import statsmodels
import statistics as stat
import scipy.stats as stats

## Opisane dane
print("Opisane dane:")
# wartość maksymalna

# wartość minimalna

# wartość oczekiwana

# mediana

# kwartyl dolny

# kwartyl górlny

# wariancja

# odchylenie standardowe

# Wartość maksymalna
print("Wartość maksymalna: ",max(vals))
# Wartość minimalna
print("Wartość minimalna: ",min(vals))
# Wartość oczekiwana
print("Wartość oczekiwana: ",stat.mean(vals))
# Mediana
print("Mediana: ",stat.median(vals))
# Kwartyl dolny
print("Kwartyl dolny: ",np.percentile(vals,25))
# Kwartyl górny
print("Kwartyl górny: ", np.percentile(vals,75))
# Wariancja
print("Wariancja: ",stat.variance(vals))
# Odchylenie standardowe
print("Odchylenie standardowe: ",stat.stdev(vals))

# Odczytujemy wcześniej zapisany plik  i oznaczmy sobie zmienne osi
df = pd.read_csv('/home/studentb10/Sprawozdanie_Dawid_Ewa/Zadanie_2/plik_b.csv')
x=df['Miesiąc']
y=df['Cena']

# Tworzymy pierwszy wykres  prezentujący ceny ropy w 2021 roku.
fig, ax = plt.subplots(figsize=(15,4))
plt.xlabel('Miesiąc')
plt.ylabel('Cena[$]')
plt.title('Ceny ropy w 2021 roku')
plt.plot(df["Cena"], marker='o')
ax.plot(x, y)
for xc in df[('Miesiąc')]:
    plt.axvline(x=xc, color='gray', linestyle='--')
    
# Na początku liczmy średnie z 3 miesięcy.
from collections import deque
n = 3
d = deque(maxlen=n)

x = [d.append(e) or sum(d)/float(n) for e in vals][n-1:]
# Funkcja policzyła średnie lecz dla każdego z miesięcy, do dalszej analizy potrzebujemt wyłącznie I,II,III,IV kwartał, dlatego odzielamy je od zbioru.
x1 = [round(x[0],2),round(x[3],2),round(x[6],2),round(x[9],2)]
print("średnia z poszczególnych kwartałów: ",x1)
#Tworzymy zmienną kwartały na potrzeby wykresu.
values = ["1","2","3","4"]

# Ponownie definiujemy zmienne
df = pd.read_csv('/home/studentb10/Sprawozdanie_Dawid_Ewa/Zadanie_2/plik_b.csv')
x=df['Miesiąc']
y=df['Cena']

# Tworzymy dwa wykresy, lecz aby zobaczyć trend umieszczony został na tle dużego wykresu mniejszy prezentujący wygładzenie liniowe dla poszczególnych kwartałów.
# Widać, iż wykres pomocniczy pokazuje trend wzrostowy.
fig, ax = plt.subplots(figsize=(16,6))
plt.xlabel('Miesiąc',size = 20)
plt.ylabel('Cena[$]', size = 20)
plt.title('Ceny ropy w 2021 roku',size = 25)
plt.plot(df["Cena"], marker='o',markersize = 8)
ax.plot(x, y)
for xc in df[('Miesiąc')]:
    plt.axvline(x=xc, color='darkgrey', linestyle='--')
ax2 = fig.add_axes([0.15, 0.560, 0.258, 0.258])
plt.xlabel('Kwartał',size = 16,)
plt.title('Wygładzenie liniowe',size = 15)
ax2.plot(values,x1,color = "dimgray", lw = 2, label = "Średnia",marker="o",linestyle='dashdot',markeredgecolor = "red",markerfacecolor = "red",markersize = 6.5)
for xc2 in values:
    plt.axvline(x=xc2, color='olive', linestyle='--')
    
print("Powyżej widać, iż trend jest wzrostowy ceny ropy w roku 2021 wzrastał z każdym miesiącem.")
print("Koniec zadania_2b")
