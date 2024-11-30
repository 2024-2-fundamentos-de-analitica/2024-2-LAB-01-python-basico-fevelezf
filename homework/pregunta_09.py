"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
    'bbb': 16,
    'ccc': 23,
    'ddd': 23,
    'eee': 15,
    'fff': 20,
    'ggg': 13,
    'hhh': 16,
    'iii': 18,
    'jjj': 18}}

    """

    letras = {}
    with open('files/input/data.csv', 'r') as file:
        for linea in file:
            columnas = linea.strip().split('\t')
            columna_5 = columnas[4].split(",")
            for item in columna_5:
                clave, valor = item.split(":")
                valor = int(valor)
                if clave in letras:
                    letras[clave] += 1 
                else:
                    letras[clave] = 1
    letras_ordenadas = dict(sorted(letras.items()))

    return letras_ordenadas

print(pregunta_09())
