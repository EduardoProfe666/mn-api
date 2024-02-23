"""
Capítulo 3. Métodos. Algoritmos de Gauss-Seidel.
Módulo que provee de los principales métodos para el algoritmo
de Gauss-Seidel
"""
from numpy import copy, zeros
import pandas as pd


class ResultadoSeidel:
    """
    Clase auxiliar que permite modelar el estado del algoritmo de Gauss-Seidel en cada iteración

    Contenido:
        lista_x: valores de x en dicha iteración
        delta: valor de delta(δ) en dicha iteración
        error: valor del error cometido en dicha iteración
        iteracion_0: si es la primera iteración de algoritmo; se usa para obviar el error y el delta en la primera iteración
    """

    def __init__(self):
        self.lista_x = []
        self.delta = 0
        self.error = 0
        self.iteracion_0 = False


def gauss_seidel(a, b, x0, f_convergencia, tol, max_iter):
    """
    Descripción:
    ---------------
        Implementación del algoritmo de Gauss-Seidel para dar solución
        a sistemas de ecuaciones lineales de orden n en la forma
        AX=B con error menor que ε

    Parámetros:
    ----------------
        a: matriz de los coeficientes de A (AX=B)

        b: matriz de los términos independientes B (AX=B)

        x0: matriz columna que representa los valores estimados de solución (se puede utilizar la matriz trivial) [Debe tener el dtype=float como en el ejemplo]

        f_convergencia: define el factor de convergencia α de la matriz A (AX=B)

        tol: cota para el error absoluto

        max_iter: cantidad máxima de iteraciones

    Salida:
    ------------
        list[ResultadoSeidel]: resultados del algoritmo de Gauss-Seidel


    Ejemplo:
    -------------
        >> from numpy import array

        >> a = array([[5, -1, 1],
           [2, 5, -1],
           [-1, 1, 5]])

        >> b = array([10, 12, 10])

        >> x0 = array([0, 0, 0], dtype=float)

        >> tol = 0.005

        >> max_iter = 100

        >> f_convergencia = 0.4

        >> r = gauss_seidel(a, b, x0, f_convergencia, tol, max_iter)

        >> # Ver métodos para convertir los resultados

    :param a: Matriz de los coeficientes de A (AX=B)
    :param b: Matriz de los términos independientes B (AX=B)
    :param x0: Matriz columna que representa los valores estimados de solución (se puede utilizar la matriz trivial)
    :param f_convergencia: Factor de convergencia α de la matriz A (AX=B)
    :param tol: Cota para el error absoluto
    :param max_iter: Cantidad máxima de iteraciones
    """
    paso = 1
    resultado = copy(x0)
    error = zeros(a.shape[1])
    condicion = True
    retorno = []
    r = ResultadoSeidel()

    r.iteracion_0 = True
    r.lista_x = error.tolist()
    retorno.append(r)

    while condicion:
        r = ResultadoSeidel()
        for i in range(a.shape[0]):
            valor_temp = 0
            for j in range(a.shape[1]):
                if i == j:
                    valor_temp += b[i] / a[i][j]
                else:
                    valor_temp += -a[i][j] / a[i][i] * resultado[j]
            error[i] = abs(resultado[i] - valor_temp)
            resultado[i] = valor_temp

        r.lista_x = resultado.tolist()
        r.delta = max(error)
        r.error = max(error) * abs(f_convergencia / (1 - f_convergencia))
        retorno.append(r)

        paso += 1
        condicion = max(error) > tol and paso <= max_iter

    return retorno


def convertir_headers_resultados_seidel(lista_resultados_seidel):
    """
    Método que permite crear los headers de la tabla de los resultados de Gauss-Seidel

    :param lista_resultados_seidel: Lista de resultados de Gauss-Seidel proveniente del método <gauss_seidel>
    """
    lista = []

    r = lista_resultados_seidel[0]
    for i in range(len(r.lista_x)):
        lista.append(f'X{i + 1}')
    lista.append('Delta(δ)')
    lista.append('Error')

    return lista


def convertir_resultados_seidel(lista_resultados_seidel):
    """
    Descripción:
    ----------------
        Permite procesar el resultado del algoritmo de Gauss-Seidel en una tabla (DataFrame de pandas)

    Parámetros:
    ----------------
        lista_resultados_seidel: lista de iteraciones que modela la clase ResultadoSeidel

    Salida:
    ----------------
        DataFrame: tabla con el resultado del algoritmo de Gauss-Seidel de forma ordenada

    Ejemplo:
    -----------------
        >> from tabulate import tabulate

        >> from numpy import array

        >> a = array([[5, -1, 1],
           [2, 5, -1],
           [-1, 1, 5]])

        >> b = array([10, 12, 10])

        >> x0 = array([0, 0, 0], dtype=float)

        >> tol = 0.005

        >> max_iter = 100

        >> f_convergencia = 0.4

        >> r = gauss_seidel(a, b, x0, f_convergencia, tol, max_iter)

        >> dataframe = convertir_resultados_seidel(r)

        >> print(tabulate(dataframe, headers="keys", tablefmt="fancy_grid"))

    :param lista_resultados_seidel: Lista de iteraciones que modela la clase ResultadoSeidel
    """
    lista = []
    for r in lista_resultados_seidel:
        l = []
        if r.iteracion_0:
            for x in r.lista_x:
                l.append(x)
            l.append('-------')
            l.append('-------')
        else:
            for x in r.lista_x:
                l.append(x)
            l.append('{:.7f}'.format(r.delta))
            l.append('{:.7f}'.format(r.error))

        lista.append(l)

    df = pd.DataFrame(data=lista, columns=convertir_headers_resultados_seidel(lista_resultados_seidel))
    df.index.name = 'Iteración'
    return df
