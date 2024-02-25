"""
Capítulo 2. Resolución de ecuaciones algebraicas. Secantes.
Módulo que provee de los métodos para el algoritmo de Secantes para la resolución
de ecuaciones algebraicas
"""

import pandas as pd


class ResultadoSecantes:
    """
    Clase que permite modelar el estado del algoritmo de Secantes en cada iteración

    Contenido:
        x: valor de x
        fx: valor de f(x)
        error: valor del error cometido en dicha iteración
        primera_iter: si es la primera iteración de algoritmo; se usa para obviar el error en la primera iteración
    """

    def __init__(self, x, fx, error, primera_iter):
        self.x = x
        self.fx = fx
        self.error = error
        self.primera_iter = primera_iter


def secantes(f, x0, x1, tol):
    """
    Descripción:
    ---------------
        Implementación del algoritmo de Secantes para aproximar raíces

    Descripción e hipótesis del algoritmo:
    ----------------------------------------
        Método iterativo de puntos. El método es una modificación de Newton-Raphson
        para eliminar la necesidad de utilizar la función derivada, sustituyendo la
        pendiente de una tangente por la pendiente de una secante. Las aproximaciones
        no hay que tomarlas obligatoriamente a un mismo lado de la raíz, ni en un orden
        específico.

        Las hipótesis son:

        - En [a,b] la ecuación posee raíz única

        - f(x) es continua en [a,b]

        - f(a)*f(b) < 0

        - f'(x) y f''(x) son continuas y no nulas en [a,b]


    Parámetros:
    ----------------
        f: función f(x) a evaluar. Es una función lambda

        x0: define uno de los extremos x0 del intervalo

        x1: define uno de los extremos x1 del intervalo

        tol: cota para el error absoluto

    Salida:
    ------------
        list[list | float]: El primer elemento ([0]) es el listado de ResultadoSecantes, el segundo elemento ([1])
        es la raíz hallada

    Ejemplo:
    -------------
        >> import math

        >> f = lambda x : x*math.e**x-2

        >> x0 = 1

        >> x1 = 0

        >> tol = 0.0005

        >> r = secantes(f, x0, x1, tol)

        >> print('Raíz hallada con método de Secantes: {:.7f}'.format(r[1]))

        Raíz hallada con método de Secantes: 0.8526055

    :param f: Función f(x) a evaluar. Es una función lambda
    :param x0: Define uno de los extremos x0 del intervalo
    :param x1: Define uno de los extremos x1 del intervalo
    :param tol: Cota para el error absoluto
    """
    if f(x0) * f(x1) >= 0.0:
        raise ValueError("La función debe cambiar de signo en el intervalo")
    if tol <= 0:
        raise ValueError("La cota de error debe ser un número positivo")

    f_x0 = f(x0)
    f_x1 = f(x1)
    error = tol + 1
    xr = 0.0
    retorno = [[]]
    retorno[0].append(ResultadoSecantes(x0, f_x0, 0, True))
    retorno[0].append(ResultadoSecantes(x1, f_x1, 0, True))

    while error > tol:
        xr = x1 - ((x1 - x0) / (f_x1 - f_x0)) * f_x1
        f_xr = f(xr)
        error = abs(xr - x1)
        retorno[0].append(ResultadoSecantes(xr, f_xr, error, False))

        x0 = x1
        f_x0 = f(x0)
        x1 = xr
        f_x1 = f(x1)

    retorno.append(xr)
    return retorno


def convertir_resultados_secantes(lista_resultados_secantes):
    """
    Descripción:
    ----------------
        Permite procesar el resultado del algoritmo de Secantes en una tabla (DataFrame de pandas)

    Parámetros:
    ----------------
        lista_resultados_secantes: lista de iteraciones que modela la clase ResultadoSecantes

    Salida:
    ----------------
        DataFrame: tabla con el resultado del algoritmo de Secantes de forma ordenada

    Ejemplo:
    -----------------
        >> from tabulate import tabulate

        >> import math

        >> f = lambda x : x*math.e**x-2

        >> x0 = 1

        >> x1 = 0

        >> tol = 0.0005

        >> r = secantes(f, x0, x1, tol)

        >> dataframe = convertir_resultados_secantes(r[0])

        >> print(tabulate(dataframe, headers="keys", tablefmt="fancy_grid"))

    :param lista_resultados_secantes: Lista de iteraciones que modela la clase ResultadoSecantes
    """
    lista = []
    for r in lista_resultados_secantes:
        l = ['{:.7f}'.format(r.x), '{:.7f}'.format(r.fx)]
        if r.primera_iter:
            l.append('---------')
        else:
            l.append('{:.7f}'.format(r.error))
        lista.append(l)

    df = pd.DataFrame(data=lista, columns=['xi', 'f(x)', 'Em(x)'])
    df.index.name = 'Iteración'
    return df
