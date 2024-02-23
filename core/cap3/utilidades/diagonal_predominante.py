"""
Capítulo 3. Utilidades. Diagonal Predominante.
Módulo que provee de los principales algoritmos que permiten conocer
si una matriz tiene diagonal predominante
"""
from numpy import absolute


def determinar_matriz_diagonal_predominante(a):
    """
    Descripción:
    -----------------
    Permite determinar si la matriz A tiene diagonal predominante

    Parámetros:
    ----------------
        a: array de numpy que representa la matriz de los coeficientes A (AX=B)

    Salida:
    --------------
        bool: la matriz tiene diagonal predominante o no

    Ejemplo:
    --------------
        >> from numpy import array

        >> import pandas as pd

        >> from tabulate import tabulate

        >> a = array([[5, -1, 1],
           [2, 5, -1],
           [-1, 1, 5]])

        >> boo = determinar_matriz_diagonal_predominante(a)

        >> print('La matriz proporcionada NO tiene diagonal predominante.') if not boo else print('La matriz tiene diagonal predominante')

    :param a: Array de numpy que representa la matriz de los coeficientes A (AX=B)
    """
    m = absolute(a)
    for i in range(len(m)):
        x = m[i][i]
        total = sum(m[i]) - x
        if x <= total:
            return False

    return True
