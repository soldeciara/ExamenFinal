from funciones import ptamlista, raiz


def fileManipulation(a, b):
    try:
        fileWrite = "my_files/notas.txt"
        file = open(fileWrite, "a+")
        file = open("my_files/notas.txt", "w")
        file.write(a)
        file.write("\n")
        file.write(b)
        file = open("my_files/notas.txt", "r")
        print("El contenido de mi archivo"
              " notas.txt es {} ".format(file.read()))
        file.close()
    except OSError as err:
        print("Error de lectura: {}".format(err))


listanum = ptamlista()
listanume = str(listanum)
listacuadrados = str(raiz(listanum))
fileManipulation(listanume, listacuadrados)
