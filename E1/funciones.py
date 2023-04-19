import random

list_valores = []


def prandom(min, max, cant):
    for i in range(0, cant):
        list_valores.append(random.randint(min, max))
    return list_valores


def prepetidos(a):
    result = []
    for item in a:
        if item not in result:
            result.append(item)
    return result


def pordena(a):
    a.sort()
    return a
