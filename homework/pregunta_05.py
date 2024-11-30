"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
    letras = {}
    with open('files/input/data.csv', 'r') as file:
        for linea in file:
            primera = linea[0]
            columnas = linea.split('\t')
            valor = int(columnas[1])
            if primera in letras:
                maximo , minimo = letras[primera]
                letras[primera] = max(maximo, valor), min(minimo, valor)
            else:
                letras[primera] = valor , valor

        organizado = [(letra, maximo, minimo) for letra, (maximo, minimo) in sorted(letras.items())]
    return (organizado)

print(pregunta_05())    
