"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]


    """

    resultado = []
    with open('files/input/data.csv', 'r') as file:
        for linea in file:
            columnas = linea.strip().split('\t')
            letra_columna_1 = columnas[0]
            elementos_columna_4 = len(columnas[3].split(","))
            elementos_columna_5 = len(columnas[4].split(","))
            resultado.append((letra_columna_1, elementos_columna_4, elementos_columna_5))

    return resultado


print(pregunta_10())