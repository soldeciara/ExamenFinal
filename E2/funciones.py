import random
import math


list_valores = []


def ptamlista():
    tam = input("Ingrese el tamaño de la lista de valores aleatorios: ")
    for i in range(0, int(tam)):
        list_valores.append(random.randint(0, 20))
    return list_valores


def raiz(a):
    r = []
    for i in range(len(a)):
        r.append(math.sqrt(a[i]))
    return r
