from collections import Counter

import pandas
import math
import tabulate
from matplotlib import pyplot as plt

k = 15

col_name = ['Długość Działki Kielicha(cm)', 'Szerokość Działki Kielicha(cm)', 'Długość Płatka(cm)',
            'Szerokość Płatka(cm)', 'Gatunek']

train = pandas.read_csv('data_train.csv', names=col_name, dtype=float)
test = pandas.read_csv('data_test.csv', names=col_name, dtype=float)

main_train_list = [train[col_name[x]].tolist() for x in range(5)]
main_test_list = [test[col_name[x]].tolist() for x in range(5)]

main_train_species_name = [train[col_name[4]].tolist()]
main_test_species_name = [test[col_name[4]].tolist()]


def Normalize(minimum, maksimum, argument):
    return (argument - minimum) / (maksimum - minimum)  # zakres 0-1


def Normalize_Data(data, min_max_list):
    for i in range(len(data) - 1):
        for j in range(len(data[i])):
            data[i][j] = Normalize(min_max_list[i * 2], min_max_list[i * 2 + 1], data[i][j])
    return data


def Min_Max_List():
    min_max_list = []
    for i in range(len(main_train_list) - 1):
        min_max_list.append(min(main_train_list[i]))
        min_max_list.append(max(main_train_list[i]))
    return min_max_list


# Dystan euklidesowy, który można stosować do dowolnej ilości wymiarów my będziemy wykorzystywać 2 i 4.
def Euclidean_Distance(*coords):
    return math.sqrt(sum([(coords[i] - coords[i + 1]) ** 2 for i in range(0, len(coords), 2)]))


# Lista zawierająca dystans między punktami w zależności od ilości argumentów.
def Distance_List(*args):
    lista_odleglosci = []
    for i in range(len(args[0])):
        coords = [args[j][i] if j % 2 == 0 else args[j] for j in range(len(args))]
        lista_odleglosci.append(Euclidean_Distance(*coords))
    return lista_odleglosci

#Sprawdza która grupa najczęściej występuje i do której należy Testowy punkt
def Which_Spesies_Group(lista):
    ileSetosa = 0
    ileVersicolor = 0
    ileVirginica = 0


    for i in range(len(lista)):
        species = int(main_train_species_name[0][lista[i]])

        match species:
            case 0:
                ileSetosa += 1
            case 1:
                ileVersicolor += 1
            case 2:
                ileVirginica += 1

    max_count = max(ileSetosa, ileVersicolor, ileVirginica)
    if max_count == ileSetosa:
        return 0
    elif max_count == ileVersicolor:
        return 1
    elif max_count == ileVirginica:
        return 2
    else:
        return 3



def KNN(distance, k):
    smallest_list_of_indexs_for_k = []

    for j in range(k):
        min_index = distance.index(min(distance))
        smallest_list_of_indexs_for_k.append(min_index)
        distance[min_index] = math.inf  # Ustawiamy wartość na nieskończoność, aby nie była wybierana ponownie

    #Sprawdzimy do jakiego gatunku należy dany punkt
    species = Which_Spesies_Group(smallest_list_of_indexs_for_k)
    match species:
        case 0 | 1 | 2:
            return species
        case 3:
            return KNN(distance, k - 1)


def KNN_Exe(four_dim, arg1, arg2):
    Success_Rate_RAW.clear()
    Success_Rate.clear()

    for i in range(1, k + 1):
        Spesies_Type_KNN = []
        How_Many_Good = 0

        Setos = 0
        Good_Versicolor = 0
        Good_Virginica = 0



        if four_dim:
            for j in range(len(main_test_list[0])):
                Spesies_Type_KNN.append(KNN(Distance_List(main_train_list[0], main_test_list[0][j], main_train_list[1],
                                             main_test_list[1][j], main_train_list[2], main_test_list[2][j],
                                             main_train_list[3], main_test_list[3][j]), i))
                if Spesies_Type_KNN[j] == main_test_species_name[0][j]:
                    How_Many_Good += 1


            Success_Rate_RAW.append(How_Many_Good)


        else:
            for j in range(len(main_test_list[0])):
                Spesies_Type_KNN.append(KNN(Distance_List(main_train_list[arg1], main_test_list[arg1][j],
                                            main_train_list[arg2], main_test_list[arg2][j]), i))
                if Spesies_Type_KNN[len(Spesies_Type_KNN) - 1] == main_test_species_name[0][j]:
                    How_Many_Good += 1

            Success_Rate_RAW.append(How_Many_Good)

        Spesies_Type_KNN.clear()

def confusion_matrix_knn(k, four_dim, arg1, arg2):
    # Inicjalizacja macierzy pomyłek jako listy list
    confusion_matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    # Przechodzimy przez wszystkie próbki testowe
    for i in range(len(main_test_list[0])):
        # Obliczamy przewidywany gatunek dla próbki testowej
        if four_dim:
            predicted_species = KNN(Distance_List(main_train_list[0], main_test_list[0][i], main_train_list[1],
                                                  main_test_list[1][i], main_train_list[2], main_test_list[2][i],
                                                  main_train_list[3], main_test_list[3][i]), k)
        else:
            predicted_species = KNN(Distance_List(main_train_list[arg1], main_test_list[arg1][i],
                                                  main_train_list[arg2], main_test_list[arg2][i]), k)
        # Obliczamy prawdziwy gatunek dla próbki testowej
        true_species = int(main_test_species_name[0][i])

        # Aktualizujemy odpowiednią komórkę w macierzy pomyłek
        confusion_matrix[predicted_species][true_species] += 1

    # Zwracamy macierz pomyłek
    return confusion_matrix


def Plot_and_matrix(four_dim, arg1, arg2):
    KNN_Exe(four_dim, arg1, arg2)


    for i in range(len(Success_Rate_RAW)):
        Success_Rate.append((Success_Rate_RAW[i] / len(main_test_list[0])) * 100)

    best_k = Success_Rate.index(max(Success_Rate))

    # Dla 4 wartości
    plt.plot(range(1, 16), Success_Rate)
    plt.xlabel('k')
    plt.xticks([x for x in range(0, 16)])
    plt.ylabel('Wynik [%]')

    matrix = confusion_matrix_knn(len(Success_Rate_RAW), four_dim, arg1, arg2)

    table = {
        "k = " + str(best_k + 1) + "     Rozpoznanie\n   Faktyczna klasa v ": ["Setosa", "Versicolor",
                                                                                               "Virginica"],
        "Setosa": matrix[0],
        "Versicolor": matrix[1],
        "Virginica": matrix[2]
    }

    if four_dim:
        print("Dla czterech parametrow")
    else:
        print(col_name[arg1] + " i " + col_name[arg2])

    print(tabulate.tabulate(table, headers="keys", tablefmt="fancy_grid", showindex=False))

    for i in range(1):
        print()

    Success_Rate_RAW.clear()
    Success_Rate.clear()

    plt.show()




# Normalizacja danych na przedział <0,1>
min_max_list = Min_Max_List()
main_train_list = Normalize_Data(main_train_list, min_max_list)
main_test_list = Normalize_Data(main_test_list, min_max_list)

Success_Rate_RAW = []
Success_Rate = []

Plot_and_matrix(True, 0, 0)
Plot_and_matrix(False, 0, 1)
Plot_and_matrix(False, 0, 2)
Plot_and_matrix(False, 0, 3)
Plot_and_matrix(False, 1, 2)
Plot_and_matrix(False, 1, 3)
Plot_and_matrix(False, 2, 3)


