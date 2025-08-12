import matplotlib.pyplot as plt
import math
import csv

# Funkcjie służące do obliczeń

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

#Pierwszy podpunkt
def suma(x):
    tak = 0.0

    for i in x:
        tak += i

    return tak


def sumaXY(x, y):
    suma = 0.0

    for i, j in zip(x, y):
        suma += i * j

    return suma


def sumaKwadratow(x):
    suma = 0.0

    for i in x:
        suma += pow(i, 2)

    return suma


def wspolczynnikKorelacjiLiniowejPearsona(x, y):
    n = len(x)

    licznik = ((n * sumaXY(x, y)) - (suma(x) * suma(y)))
    mianownik = math.sqrt(((n * sumaKwadratow(x)) - pow(suma(x), 2)) * ((n * sumaKwadratow(y)) - pow(suma(y), 2)))

    return round((licznik / mianownik), 2)


#Drugi podpunkt
def parametrA(x, y):
    sredniaX = suma(x)/len(x)
    sredniaY = suma(y)/len(y)

    return round((sredniaY - (parametrB(x, y) * sredniaX)), 1)


def parametrB(x, y):
    n = len(x)

    licznik = ((n * sumaXY(x, y)) - (suma(x) * suma(y)))
    mianownik = ((n * sumaKwadratow(x)) - pow(suma(x), 2))

    return licznik/mianownik


def rownanieRegresjiLiniowejSTR(x, y):
    a = round(parametrA(x, y), 1)
    b = round(parametrB(x, y), 1)

    if (a > 0):
        return "y = " + str(b) + "x + " + str(a)
    else:
        return "y = " + str(b) + "x + " + "(" + str(a) + ")"


def tablicaY(x, y):
    tablica = []

    for i in x:
        tablica.append(float(parametrB(x, y) * i + parametrA(x, y)))

    return tablica

def titleSTR(x, y):
    return "r = " + str(wspolczynnikKorelacjiLiniowejPearsona(x, y)) + "; " + rownanieRegresjiLiniowejSTR(x, y)


#print(wspolczynnikKorelacjiLiniowejPearsona(dlugoscDzialki, szerokoscDzialki))
#print(rownanieRegresjiLiniowejSTR(dlugoscDzialki, szerokoscDzialki))


def plot_data(axis, x, y, xlabel, ylabel):
    axis.plot(x, y, 'o')
    axis.plot(x, tablicaY(x, y), color="red")
    axis.set_title(titleSTR(x, y))
    axis.set_xlabel(xlabel)
    axis.set_ylabel(ylabel)


fig, axis = plt.subplots(3, 2)
fig.tight_layout()


plot_data(axis[0][0], dlugoscDzialki, szerokoscDzialki, "Długość działki kielicha (cm)", "Szerokość działki kielicha (cm)")
plot_data(axis[0][1], dlugoscDzialki, dlugoscPlatka, "Długość działki kielicha (cm)", "Długość płatka (cm)")
plot_data(axis[1][0], dlugoscDzialki, szerokoscPlatka, "Długość działki kielicha (cm)", "Szerokość platka (cm)")
plot_data(axis[1][1], szerokoscDzialki, dlugoscPlatka, "Szerokość działki kielicha (cm)", "Długość płatka (cm)")
plot_data(axis[2][0], szerokoscDzialki, szerokoscPlatka, "Szerokość działki kielicha (cm)", "Szerokość płatka (cm)")
plot_data(axis[2][1], dlugoscPlatka, szerokoscPlatka, "Długość płatka (cm)", "Szerokość płatka (cm)")

plt.show()