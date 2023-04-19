def funcionA(funcionB):

    def funcionC(*args, **kwargs):
        print("Está por ejecutarse la función") #Antes de ejecutar la función a decorar
        print("Valores de *args: {}".format(args))
        print("Valores de kwargs: {}".format(kwargs.items()))
        resultado = funcionB(*args, **kwargs)
        print("“La función ha sido ejecutado correctamente") #Después de ejecutar la función a decorada
        return resultado
    return funcionC


@funcionA
def multiplicar(numa, numb, numc, numd):
    mult = numa * numb * numc * numd
    print("La multiplicación es: {}".format(mult))

@funcionA
def suma(numa, numb, numc, numd, nume):
    sum = numa + numb + numc + numd + nume
    print("La suma es: {}".format(sum))

suma(4, 5, 2, 3, 8)
multiplicar(4, 5, 2, 3)
