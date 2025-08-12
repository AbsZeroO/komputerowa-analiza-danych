import random

import matplotlib.pyplot as plt
import math
import csv
import numpy as np

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

vector = np.column_stack((dlugoscDzialki, szerokoscDzialki, dlugoscPlatka, szerokoscPlatka))


def dystans(test, train):
    dyst = 0

    for i in range(len(test)):
        dyst += (test[i] - train[i]) ** 2

    return math.sqrt(dyst)


def czy_unikalne(lista):
    lista_str = [str(i) for i in lista]
    return len(lista_str) == len(set(lista_str))


def kSrednie(vector, k):
    m = []
    S = [[] for x in range(k)]
    iterajce = 0
    poprzednie = None

    for i in range(k):
        m.append(random.choice(vector))
    while not czy_unikalne(m):
        for i in range(k):
            m[i] = (random.choice(vector))

    while True:
        dystansCentPunkt = []


        # przypisanie centroidów
        for i in range(k):
            S[i] = [m[i]]

        for punkty in vector:
            dystansCentPunkt = [dystans(S[i][0], punkty) for i in range(k)]
            min_dystans_index = dystansCentPunkt.index(min(dystansCentPunkt))
            S[min_dystans_index].append(punkty)

        for i in range(k):
            m[i] = sum(S[i]) / len(S[i])

        # for i in range(k):
        #     print(i, S[i])


        iterajce += 1
        if not poprzednie is None and all(np.array_equal(poprzednie[x], S[x]) for x in range(k)):
            return iterajce, S

        poprzednie = [list(klaster) for klaster in S] #3.694377164692951

def WCSS(S, k):
    wcss = 0
    dystansCentPunkt = []

    for i in range(k):

        for j in range(1, len(S[i])):
            dystansCentPunkt += [dystans(S[i][0], S[i][j])]

        for j in range(len(dystansCentPunkt)):
            wcss += dystansCentPunkt[j]

        dystansCentPunkt.clear()

    return wcss


def kSrednichPLT(k, yesno):
    ksrednie = kSrednie(vector, k)

    if yesno == False:
        return WCSS(ksrednie[1], k), ksrednie[0]

    dlugoscDzialkiKSrednich = [[] for x in range(k)]
    szerokoscDzialkiKSrednich = [[] for x in range(k)]
    dlugoscPlatkaKSrednich = [[] for x in range(k)]
    szerokoscPlatkaKSrednich = [[] for x in range(k)]

    dlugoscDzialkiKSrednichCentroid = [[] for x in range(k)]
    szerokoscDzialkiKSrednichCentroid = [[] for x in range(k)]
    dlugoscPlatkaKSrednichCentroid = [[] for x in range(k)]
    szerokoscPlatkaKSrednichCentroid = [[] for x in range(k)]


    for i in range(k):
        for j in range(1):
            dlugoscDzialkiKSrednichCentroid[i].append(ksrednie[1][i][j][0])
            szerokoscDzialkiKSrednichCentroid[i].append(ksrednie[1][i][j][1])
            dlugoscPlatkaKSrednichCentroid[i].append(ksrednie[1][i][j][2])
            szerokoscPlatkaKSrednichCentroid[i].append(ksrednie[1][i][j][3])

    for i in range(k):
        for j in range(1, len(ksrednie[1][i])):
            dlugoscDzialkiKSrednich[i].append(ksrednie[1][i][j][0])
            szerokoscDzialkiKSrednich[i].append(ksrednie[1][i][j][1])
            dlugoscPlatkaKSrednich[i].append(ksrednie[1][i][j][2])
            szerokoscPlatkaKSrednich[i].append(ksrednie[1][i][j][3])




    kolory = ["red", "blue", "green", "yellow", "purple", "pink", "black", "grey", "orange", "brown"]

    fig, axis = plt.subplots(3, 2)
    fig.tight_layout()

    for i in range(k):
        axis[0][0].plot(dlugoscDzialkiKSrednich[i], szerokoscDzialkiKSrednich[i], 'o', color=kolory[i],
                        fillstyle="none")
        axis[0][0].plot(dlugoscDzialkiKSrednichCentroid[i], szerokoscDzialkiKSrednichCentroid[i], 'D', color=kolory[i])

    axis[0][0].set_xlabel("Długość działki kielicha (cm)")
    axis[0][0].set_ylabel("Szerokość działki kielicha (cm)")

    for i in range(k):
        axis[0][1].plot(dlugoscDzialkiKSrednich[i], dlugoscPlatkaKSrednich[i], 'o', color=kolory[i], fillstyle="none")
        axis[0][1].plot(dlugoscDzialkiKSrednichCentroid[i], dlugoscPlatkaKSrednichCentroid[i], 'D', color=kolory[i])

    axis[0][1].set_xlabel("Długość działki kielicha (cm)")
    axis[0][1].set_ylabel("Długość płatka (cm)")

    for i in range(k):
        axis[1][0].plot(dlugoscDzialkiKSrednich[i], szerokoscPlatkaKSrednich[i], 'o', color=kolory[i], fillstyle="none")
        axis[1][0].plot(dlugoscDzialkiKSrednichCentroid[i], szerokoscPlatkaKSrednichCentroid[i], 'D', color=kolory[i])

    axis[1][0].set_xlabel("Długość działki kielicha (cm)")
    axis[1][0].set_ylabel("Szerokość platka (cm)")

    for i in range(k):
        axis[1][1].plot(szerokoscDzialkiKSrednich[i], dlugoscPlatkaKSrednich[i], 'o', color=kolory[i], fillstyle="none")
        axis[1][1].plot(szerokoscDzialkiKSrednichCentroid[i], dlugoscPlatkaKSrednichCentroid[i], 'D', color=kolory[i])

    axis[1][1].set_xlabel("Szerokość działki kielicha (cm)")
    axis[1][1].set_ylabel("Długość płatka (cm)")


    for i in range(k):
        axis[2][0].plot(szerokoscDzialkiKSrednich[i], szerokoscPlatkaKSrednich[i], 'o', color=kolory[i],
                        fillstyle="none")
        axis[2][0].plot(szerokoscDzialkiKSrednichCentroid[i], szerokoscPlatkaKSrednichCentroid[i], 'D', color=kolory[i])

    axis[2][0].set_xlabel("Szerokość działki kielicha (cm)")
    axis[2][0].set_ylabel("Szerokość płatka (cm)")

    for i in range(k):
        axis[2][1].plot(dlugoscPlatkaKSrednich[i], szerokoscPlatkaKSrednich[i], 'o', color=kolory[i], fillstyle="none")
        axis[2][1].plot(dlugoscPlatkaKSrednichCentroid[i], szerokoscPlatkaKSrednichCentroid[i], 'D', color=kolory[i])

    axis[2][1].set_xlabel("Długość płatka (cm)")
    axis[2][1].set_ylabel("Szerokość płatka (cm)")

    plt.show()

    return WCSS(ksrednie[1], k), ksrednie[0]