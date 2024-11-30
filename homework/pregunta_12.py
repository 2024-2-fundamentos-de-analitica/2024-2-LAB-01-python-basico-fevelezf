"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
    suma_por_letra = {}
    with open('files/input/data.csv', 'r') as file:
        for linea in file:
            columnas = linea.strip().split('\t')
            valores = columnas[4].split(",")
            for v in valores:
                valores_partidos = v.split(":")
                numero = int(valores_partidos[1])

                #valor_columna_2 = int(columnas[4])
                letras_columna_4 = columnas[0]
                for letra in letras_columna_4:
                    if letra in suma_por_letra:
                        suma_por_letra[letra] += numero
                    else:
                        suma_por_letra[letra] = numero
        suma_por_letra_ordenada = dict(sorted(suma_por_letra.items()))

        return suma_por_letra_ordenada

print(pregunta_12())