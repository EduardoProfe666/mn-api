"""
Capítulo 4. Aproximación de funciones. Método de Newton o Diferencias Divididas.
Módulo que provee de los métodos para el algoritmo de Newton (Diferencias Divididas)
para interpolación polinómica
"""
import pandas as pd
from numpy import zeros


def newton_diff(xi, yi):
    """
    Descripción:
    -----------------
        Implementación del algoritmo de Newton (Diferencias Divididas) para interpolación polinómica.
        Permite calcular la tabla de las diferencias divididas.

    Descripción e hipótesis del algoritmo:
    ---------------------------------------
        La idea fundamental del método de Newton es realizar la interpolación en un punto
        de forma sucesiva: partiendo de dos nodos ir agregando los demás, uno por uno, en
        el orden que se desee, de tal manera que en cada paso solo se requiera agregar un nuevo
        término a los cálculos precedentes. El método permite, sin realizar ninguna operación
        adicional, ir obteniendo en cada paso del proceso una estimación del error de interpolación,
        de manera que el proceso iterativo se pueda detener si se alcanza un error suficientemente pequeño.

        Este método es útil para situaciones que requieran un número bajo de puntos para interpolar,
        ya que a medida que crece el número de puntos, también lo hace el grado del polinomio.

    Parámetros:
    ---------------------------------------
        xi: Array de numpy que contiene los coeficientes de xi

        yi: Array de numpy que contiene los valores de yi para cada xi

    Salida:
    ---------------------
        ndarray[Any, dtype[floating[_64Bit] | float_]]: Tabla de diferencias divididas

    Ejemplo:
    ---------------------
        >> from numpy import array

        >> xi = array([1.15, 1.20, 1.10, 1.25, 1.05, 1.30])

        >> yi = array([0.93304, 0.91817, 0.95135, 0.90640, 0.97350, 0.89747])

        >> diffs = diferencias_divididas(xi, yi)

        >> # Ver método para convertir los resultados a una tabla

    :param xi: Array de numpy que contiene los coeficientes de xi
    :param yi: Array de numpy que contiene los valores de yi para cada xi
    """
    n = len(yi)
    coef = zeros([n, n])
    coef[:, 0] = yi

    for j in range(1, n):
        for i in range(n - j):
            coef[i][j] = (coef[i + 1][j - 1] - coef[i][j - 1]) / (xi[i + j] - xi[i])
    return coef


def convertir_resultados(xi, yi, r_newton_diff):
    """
    Descripción:
    -----------------
        Permite procesar el resultado del algoritmo de Newton (Diferencias Divididas)
        en una tabla (DataFrame de pandas)

    Parámetros:
    ---------------------------------------
        xi: Array de numpy que contiene los coeficientes de xi

        yi: Array de numpy que contiene los valores de yi para cada xi

        r_newton_diff: Resultado del método de Newton (newton_diff)

    Salida:
    ---------------------
        DataFrame: Tabla con el resultado del algoritmo de forma ordenada

    Ejemplo:
    ---------------------
        >> from numpy import array

        >> xi = array([1.15, 1.20, 1.10, 1.25, 1.05, 1.30])

        >> yi = array([0.93304, 0.91817, 0.95135, 0.90640, 0.97350, 0.89747])

        >> diffs = diferencias_divididas(xi, yi)

        >> dataframe = convertir_resultados(xi, yi, diffs)

        >> print(tabulate(dataframe, headers="keys", tablefmt="fancy_grid"))

    :param xi: Array de numpy que contiene los coeficientes de xi
    :param yi: Array de numpy que contiene los valores de yi para cada xi
    :param r_newton_diff: Resultado del método de Newton (newton_diff)
    """
    lista = []
    n = len(r_newton_diff[0])
    for i, r in enumerate(r_newton_diff):
        l = ['{:.7f}'.format(xi[i]), '{:.7f}'.format(yi[i])]
        for j, diff in enumerate(r):
            if j != 0 and j < n - i:
                l.append('{:.7f}'.format(diff))
            elif j != 0:
                l.append('---------')
        lista.append(l)

    cols = ['xi', 'f(x)']
    for i in range(1, n):
        cols.append('diff ' + str(i))

    df = pd.DataFrame(data=lista, columns=cols)
    df.index.name = 'Iteración'
    return df
