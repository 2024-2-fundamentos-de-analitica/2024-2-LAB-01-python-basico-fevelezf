"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import glob
import os

def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """

    suma = 0
    with open('files/input/data.csv', 'r') as file:
        for linea in file:
            columnas = linea.split('\t')

            suma += int(columnas[1])

    return suma

print(pregunta_01())
