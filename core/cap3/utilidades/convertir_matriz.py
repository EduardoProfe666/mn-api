"""
Capítulo 3. Utilidades. Conversión de matrices.
Módulo que provee de los principales algoritmos de conversión de matrices
de la forma AX=B a la forma X=MC+C
"""
from numpy import array


def convertir_matriz_m(a):
    """
    Descripción:
    -----------------
    Permite convertir de la matriz A (AX=B) a la matriz M (X=MX+C)

    Parámetros:
    ----------------
        a: array de numpy que representa la matriz de los coeficientes A (AX=B)

    Salida:
    --------------
        ndarray[Any, dtype]: La matriz M resultante de la conversión

    Ejemplo:
    --------------
        >> import pandas as pd

        >> from tabulate import tabulate

        >> a = array([[5, -1, 1],
           [2, 5, -1],
           [-1, 1, 5]])

        >> dataframe = pd.DataFrame(data=convertir_matriz_m(a))

        >> print(tabulate(dataframe, headers="keys", tablefmt="fancy_grid"))

    :param a: Array de numpy que representa la matriz de los coeficientes A (AX=B)
    """
    matriz_m = array(a, dtype=float)
    for i in range(a.shape[0]):
        for j in range(a.shape[0]):
            if i != j:
                matriz_m[i][j] = (a[i][j] * (-1)) / a[i][i]
            else:
                matriz_m[i][i] = 0
    return matriz_m


def convertir_matriz_c(a, b, transpuesta: bool = True):
    """
    Descripción:
    -----------------
    Permite convertir de la matriz A y B (AX=B) a la matriz C (X=MX+C)

    Parámetros:
    ----------------
        a: array de numpy que representa la matriz de los coeficientes A (AX=B)

        b: array de numpy que representa la matriz de los términos independientes B (AX=B)

        transpuesta: bool que representa si el resultado se entrega en una matriz transpuesta o no

    Salida:
    --------------
        ndarray[Any, dtype]: La matriz C resultante de la conversión

    Ejemplo:
    --------------
        >> import pandas as pd

        >> from tabulate import tabulate

        >> a = array([[5, -1, 1],
           [2, 5, -1],
           [-1, 1, 5]])

        >> b = array([10, 12, 10])

        >> dataframe = pd.DataFrame(data=convertir_matriz_c(a, b))

        >> print(tabulate(dataframe, headers="keys", tablefmt="fancy_grid"))


    :param a: Array de numpy que representa la matriz de los coeficientes A (AX=B)
    :param b: Array de numpy que representa la matriz de los términos independientes B (AX=B)
    :param transpuesta: Bool que representa si el resultado se entrega en una matriz transpuesta o no
    """
    matriz_c = array(b, dtype=float)
    for i in range(b.shape[0]):
        matriz_c[i] = b[i] / a[i][i]
    return matriz_c if not transpuesta else matriz_c.transpose()
