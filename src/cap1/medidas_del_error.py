"""
Capítulo 1. Medidas del error.
Módulo que provee de los principales algoritmos de medidas del error
"""


def error(x: float, xa: float):
    """
    Permite calcular el error del valor aproximado con respecto al valor exacto

    Parámetros:
        x: valor exacto
        xa: valor aproximado

    Salida:
        float: error del valor aproximado en relación con el valor exacto
    """

    return x - xa


def error_abs(error: float) -> float:
    """
    Permite calcular el error absoluto E(x) dado el error

    Parámetros:
        error: error del valor aproximado xa

    Salida:
        float: error absoluto
    """

    return abs(error)


def error_rel(error_abs: float, x: float):
    """
    Permite calcular el error relativo e(x) dado el error absoluto y el valor exacto

    Parámetros:
        error_abs: error absoluto
        x: valor exacto

    Salida:
        float: error relativo
    """

    return error_abs / abs(x)


def min_error_abs_max(a: float, b: float):
    """
    Permite obtener el mínimo error absoluto máximo Em(x) en el intervalo [a,b]

    Parámetros:
        a: punto inicial del intervalo [a,b]
        b: punto final del intervalo [a,b]

    Salida:
        float: mínimo error absoluto máximo
    """

    return (a + b) / 2
