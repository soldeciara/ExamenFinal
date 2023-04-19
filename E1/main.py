from funciones import prandom, prepetidos, pordena

lista = prandom(0, 5, 10)
print("Lista de valores random: {}".format(lista))
print("Lista de valores sin repetidos: {}".format(prepetidos(lista)))
print("Lista de valores ordenados de "
      "menor a mayor: {}".format(pordena(prepetidos(lista))))
print("Lista de valores ordenados "
      "de mayor a menor: {}".format(sorted(pordena(prepetidos(lista)),
                                           reverse=True)))
