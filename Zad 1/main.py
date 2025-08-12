from tabulate import tabulate
import matplotlib.pyplot as plt
import math
import csv


#Funkcjie służące do obliczeń

def minimum(tablica):
    najmniejsza = None

    for i in tablica:
        if najmniejsza is None or najmniejsza > i:
            najmniejsza = i

    return najmniejsza

def maksimum(tablica):
    najwieksza = None

    for i in tablica:
        if najwieksza is None or najwieksza < i:
            najwieksza = i

    return najwieksza

def sredniaArytmetyczna(tablica):
    srednia = 0
    for i in tablica:
        srednia += i

    return srednia/len(tablica)

def odchyStand(tablica):
    srednia = sredniaArytmetyczna(tablica)
    suma = 0

    for i in tablica:
        suma += pow((i - srednia),2)

    return math.sqrt(suma/(len(tablica)-1))

def mediana(tablica):

    n = len(tablica)
    if n % 2 == 0:
        return (tablica[n // 2] + tablica[n // 2 - 1]) / 2
    else:
        return tablica[n // 2]

def medianaQ1(tablica):

    n = len(tablica)
    q1 = (n // 4)
    if n % 2 == 0:
        return (tablica[q1] + tablica[q1 - 1]) / 2
    else:
        return tablica[q1]

def medianaQ3(tablica):

    n = len(tablica)
    q3 = (3 * n // 4)
    if n % 2 == 0:
        return (tablica[q3] + tablica[q3 - 1]) / 2
    else:
        return tablica[q3]

#Funkcje służące do wypisywania

def minimumSTR(wartosc):
    return '%.2f' % minimum(wartosc)

def sredniaOdchSTR(wartosc):
    return '%.2f' % sredniaArytmetyczna(wartosc) + "(±" + '%.2f' % odchyStand(wartosc) + ")"

def medianaSTR(wartosc):
    return '%.2f' % mediana(wartosc) + "(" + '%.2f' % medianaQ1(wartosc) + "-" + '%.2f' % medianaQ3(wartosc) + ")"

def maksimumSTR(wartosc):
    return '%.2f' % maksimum(wartosc)



ileSetosa = 0
ileVersicolor = 0
ileVirginica = 0

dlugoscDzialki = []
szerokoscDzialki = []
dlugoscPlatka = []
szerokoscPlatka = []

dlugoscDzialkiSetosa = []
szerokoscDzialkiSetosa = []
dlugoscPlatkaSetosa = []
szerokoscPlatkaSetosa = []

dlugoscDzialkiVersicolor = []
szerokoscDzialkiVersicolor = []
dlugoscPlatkaVersicolor = []
szerokoscPlatkaVersicolor = []

dlugoscDzialkiVirginica = []
szerokoscDzialkiVirginica = []
dlugoscPlatkaVirginica = []
szerokoscPlatkaVirginica = []

with open('data.csv', 'r', encoding='UTF-8') as datafile:
    data = csv.reader(datafile, delimiter=',')

    for row in data:
        kwiatek = row[4]
        match kwiatek:
            case '0':
                ileSetosa += 1
                dlugoscDzialkiSetosa.append(float(row[0]))
                szerokoscDzialkiSetosa.append(float(row[1]))
                dlugoscPlatkaSetosa.append(float(row[2]))
                szerokoscPlatkaSetosa.append(float(row[3]))
            case '1':
                ileVersicolor += 1
                dlugoscDzialkiVersicolor.append(float(row[0]))
                szerokoscDzialkiVersicolor.append(float(row[1]))
                dlugoscPlatkaVersicolor.append(float(row[2]))
                szerokoscPlatkaVersicolor.append(float(row[3]))
            case '2':
                ileVirginica += 1
                dlugoscDzialkiVirginica.append(float(row[0]))
                szerokoscDzialkiVirginica.append(float(row[1]))
                dlugoscPlatkaVirginica.append(float(row[2]))
                szerokoscPlatkaVirginica.append(float(row[3]))


        dlugoscDzialki.append(float(row[0]))
        szerokoscDzialki.append(float(row[1]))
        dlugoscPlatka.append(float(row[2]))
        szerokoscPlatka.append(float(row[3]))



ileWszystkich = ileVirginica + ileVersicolor + ileSetosa

#Liczebność podawana w %
liczebnoscSetosa = round(ileSetosa/ileWszystkich * 100, 1)
liczebnoscVersicolor = round(ileVersicolor/ileWszystkich * 100, 1)
liczebnoscVirginica = round(ileVirginica/ileWszystkich * 100, 1)
liczebnoscWszystkich = round(ileWszystkich/ileWszystkich * 100, 1)

#Dane połączone by przedstawić je ładnie w tabeli
setosDane = str(ileSetosa) + "(" + str(liczebnoscSetosa) + "%)"
versicolorDane = str(ileVersicolor) + "(" + str(liczebnoscVersicolor) + "%)"
virginicaDane = str(ileVirginica) + "(" + str(liczebnoscVirginica) + "%)"
razemDane = str(ileWszystkich) + "(" + str(liczebnoscWszystkich) + "%)"

tabelHeader = ['Gatunek', 'Liczebność(%)']
tabelData = [['Setosa', setosDane],
             ['Versicolor', versicolorDane],
             ['Virginica', virginicaDane],
             ['Razem', razemDane]]
print(tabulate(tabelData, headers=tabelHeader, tablefmt="pretty"))


tabel2Header = ['Cecha', 'Minimum', 'Śr.arytm.(±odch.stand.)', 'Mediana(Q1-Q3)', 'Maksimum']
tabel2Data = [['Długość działki kielicha (cm)', minimumSTR(dlugoscDzialki), sredniaOdchSTR(dlugoscDzialki), medianaSTR(sorted(dlugoscDzialki)), maksimumSTR(dlugoscDzialki)],
              ['Szerokość działki kielicha (cm)', minimumSTR(szerokoscDzialki), sredniaOdchSTR(szerokoscDzialki), medianaSTR(sorted(szerokoscDzialki)), maksimumSTR(szerokoscDzialki)],
              ['Długość płatka (cm)', minimumSTR(dlugoscPlatka), sredniaOdchSTR(dlugoscPlatka), medianaSTR(sorted(dlugoscPlatka)), maksimumSTR(dlugoscPlatka)],
              ['Szerokość płatka (cm)', minimumSTR(szerokoscPlatka), sredniaOdchSTR(szerokoscPlatka), medianaSTR(sorted(szerokoscPlatka)), maksimumSTR(szerokoscPlatka)]]
print(tabulate(tabel2Data, headers=tabel2Header, tablefmt="pretty"))

#Napisać funkcje do Histogramów

def histogram(tablica, binsTable):

    counts = [0 for i in binsTable]
    for value in tablica:
        for i in range(len(binsTable)-1):
            if binsTable[i] <= value < binsTable[i + 1]:
                counts[i] += 1

    return binsTable, counts


#Histogramy
fig, axis = plt.subplots(4, 2)
fig.tight_layout()
hist0 = histogram(dlugoscDzialki, [4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0])

axis[0][0].bar(hist0[0], hist0[1], ec="black", width=0.5, align="edge")
axis[0][0].set_xticks([4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0])
axis[0][0].set_title("Długość działki kielicha")
axis[0][0].set_xlabel("Długość (cm)")
axis[0][0].set_ylabel("Liczebność")

axis[0][1].boxplot([dlugoscDzialkiSetosa, dlugoscDzialkiVersicolor, dlugoscDzialkiVirginica], labels=['Setosa', 'Versicolor', 'Virginica'])
axis[0][1].set_xlabel("Gatunek")
axis[0][1].set_ylabel("Długość (cm)")
#/////////////////////////////////////////////////////////////////////////////////////////////////#

hist1 = histogram(szerokoscDzialki, [2.0, 2.2, 2.4, 2.6, 2.8, 3.0, 3.2, 3.4, 3.6, 3.8,  4.0, 4.2, 4.4])
axis[1][0].bar(hist1[0], hist1[1], ec="black", width=0.2, align="edge")
axis[1][0].set_xticks([2.0, 2.2, 2.4, 2.6, 2.8, 3.0, 3.2, 3.4, 3.6, 3.8,  4.0, 4.2, 4.4])
axis[1][0].set_title("Szerokość działki kielicha")
axis[1][0].set_xlabel("Szerokość (cm)")
axis[1][0].set_ylabel("Liczebność")

axis[1][1].boxplot([szerokoscDzialkiSetosa, szerokoscDzialkiVersicolor, szerokoscDzialkiVirginica], labels=['Setosa', 'Versicolor', 'Virginica'])
axis[1][1].set_xlabel("Gatunek")
axis[1][1].set_ylabel("Szerokość (cm)")
#/////////////////////////////////////////////////////////////////////////////////////////////////#

hist2 = histogram(dlugoscPlatka, [1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0])
axis[2][0].bar(hist2[0], hist2[1], ec="black", width=0.5, align="edge")
axis[2][0].set_xticks([1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0])
axis[2][0].set_title("Długość Płatka")
axis[2][0].set_xlabel("Długość (cm)")
axis[2][0].set_ylabel("Liczebność")

axis[2][1].boxplot([dlugoscPlatkaSetosa, dlugoscPlatkaVersicolor, dlugoscPlatkaVirginica], labels=['Setosa', 'Versicolor', 'Virginica'])
axis[2][1].set_xlabel("Gatunek")
axis[2][1].set_ylabel("Długość (cm)")
#/////////////////////////////////////////////////////////////////////////////////////////////////#

hist3 = histogram(szerokoscPlatka, [0.0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0, 2.2, 2.4, 2.6])
axis[3][0].bar(hist3[0], hist3[1], ec="black", width=0.2, align="edge")
axis[3][0].set_xticks([0.0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0, 2.2, 2.4, 2.6])
axis[3][0].set_title("Szerokość Płatka")
axis[3][0].set_xlabel("Szerokość (cm)")
axis[3][0].set_ylabel("Liczebność")

axis[3][1].boxplot([szerokoscPlatkaSetosa, szerokoscPlatkaVersicolor, szerokoscPlatkaVirginica], labels=['Setosa', 'Versicolor', 'Virginica'])
axis[3][1].set_xlabel("Gatunek")
axis[3][1].set_ylabel("Szerokość (cm)")

for i in range(4):
    for j in range(2):
        axis[i][0].set_yticks([x for x in range(0, 36, 5)])
        axis[i][j].grid(axis="y")
        axis[i][j].set_axisbelow(True)



########################################################################################################################
########################################################################################################################

fig, axis = plt.subplots(4)
fig.tight_layout()

#Informacje o Cechach

histCombDlugoscDzialki = [dlugoscDzialkiSetosa, dlugoscDzialkiVersicolor, dlugoscDzialkiVirginica]
bins0 = [4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0]
for i in range(3):
    hist = histogram(histCombDlugoscDzialki[i], [4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0])

    if i > 0:
        for x in range(len(bins0)):
            bins0[x] += 0.1666

    axis[0].bar(bins0, hist[1], ec="black", width=0.1666, align="edge")

axis[0].set_xticks([4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0])
axis[0].legend(['Setosa', 'Versicolor', 'Virginica'])
axis[0].set_title("Długość działek kielichów kwiatów")
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#

histCombSzerokoscDzialki = [szerokoscDzialkiSetosa, szerokoscDzialkiVersicolor, szerokoscDzialkiVirginica]
bins1 = [2.0, 2.2, 2.4, 2.6, 2.8, 3.0, 3.2, 3.4, 3.6, 3.8,  4.0, 4.2, 4.4]
for i in range(3):
    hist = histogram(histCombSzerokoscDzialki[i], [2.0, 2.2, 2.4, 2.6, 2.8, 3.0, 3.2, 3.4, 3.6, 3.8,  4.0, 4.2, 4.4])

    if i > 0:
        for x in range(len(bins1)):
            bins1[x] += 0.0666

    axis[1].bar(bins1, hist[1], ec="black", width=0.0666, align="edge")

axis[1].set_xticks([2.0, 2.2, 2.4, 2.6, 2.8, 3.0, 3.2, 3.4, 3.6, 3.8,  4.0, 4.2, 4.4])
axis[1].legend(['Setosa', 'Versicolor', 'Virginica'])
axis[1].set_title("Szerokość działek kielichów kwiatów")
#/////////////////////////////////////////////////////////////////////////////////////////////////#

histCombDlugoscPlatka = [dlugoscPlatkaSetosa, dlugoscPlatkaVersicolor, dlugoscPlatkaVirginica]
bins2 = [1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0]
for i in range(3):
    hist = histogram(histCombDlugoscPlatka[i], [1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0])

    if i > 0:
        for x in range(len(bins2)):
            bins2[x] += 0.1666

    axis[2].bar(bins2, hist[1], ec="black", width=0.1666, align="edge")

axis[2].set_xticks([1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0])
axis[2].legend(['Setosa', 'Versicolor', 'Virginica'])
axis[2].set_title("Długość płatków kwiatów")
#/////////////////////////////////////////////////////////////////////////////////////////////////#

histCombSzerokoscPlatka = [szerokoscPlatkaSetosa, szerokoscPlatkaVersicolor, szerokoscPlatkaVirginica]
bins3 = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0, 2.2, 2.4, 2.6]
for i in range(3):
    hist = histogram(histCombSzerokoscPlatka[i], [0.0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0, 2.2, 2.4, 2.6])

    if i > 0:
        for x in range(len(bins3)):
            bins3[x] += 0.0666

    axis[3].bar(bins3, hist[1], ec="black", width=0.0666, align="edge")

axis[3].set_xticks([0.0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0, 2.2, 2.4, 2.6])
axis[3].legend(['Setosa', 'Versicolor', 'Virginica'])
axis[3].set_title("Szerokość płatków kwiatów")

for i in range(4):
    axis[i].set_yticks([x for x in range(0, 31, 5)])
    axis[i].grid(axis="y")
    axis[i].set_axisbelow(True)



plt.show()