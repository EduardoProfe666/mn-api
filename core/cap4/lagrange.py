"""
Capítulo 4. Aproximación de funciones. Método de Lagrange.
Módulo que provee de los métodos para el algoritmo de Lagrange para interpolación polinómica
"""
from sympy.abc import x


def lagrange_interpol(xi, yi, x0, simbolico):
    """
    Descripción:
    -----------------
        Implementación del algoritmo de Lagrange para interpolación polinómica.

    Descripción e hipótesis del algoritmo:
    ---------------------------------------
        Sean x0, x1, ..., xn, n+1 nodos de interpolación diferentes y f(x)
        la función a interpolar. Sean yi=f(xi)  i=0,1,2,...,n los valores
        de f en los nodos. El método de Lagrange consiste en encontrar n+1 polinomios
        básicos de grado n: L0(x), L1(x), ..., Ln(x) que satisfagan las siguientes condiciones:

        L0(x0)=1 | L1(x0)=0 | L2(x0)=0 ... Ln(x0)=0

        L0(x1)=0 | L1(x1)=1 | L2(x1)=0 ... Ln(x1)=0

        L0(x2)=0 | L1(x2)=0 | L2(x2)=1 ... Ln(x2)=0

        ···················································································

        L0(xn)=0 | L1(xn)=0 | L2(xn)=0 ... Ln(xn)=1

    Parámetros:
    ---------------------------------------
        xi: Conjunto de puntos xi (List[float])

        yi: Conjunto de puntos yi (List[float])

        x0: Aproximación de la función en un punto determinado x0 (float)

        simbolico: Determina si se realizará por cálculo simbólico (sin resultado numérico) o no (bool)

    Salida:
    ---------------------
        float | sympy_function: Resultado de la interpolación polinómica

    Ejemplo:
    -------------
        >> from sympy import simplify

        >> xi = [1, 2, 4]

        >> yi = [2, 3, 1]

        >> x0 = 2.5

        >> # Polinomio Interpolador p(x) simbólico

        >> print(lagrange_interpol(xi, yi, x0, True))

        2*(4/3 - x/3)*(2 - x) + 3*(2 - x/2)*(x - 1) + (x/3 - 1/3)*(x/2 - 1)

        >> # Polinomio Interpolador p(x) simbólico simplificado

        >> print(simplify(lagrange_interpol(xi, yi, x0, True))))

        -2*x**2/3 + 3*x - 1/3

        >> # Polinomio Interpolador en un punto p(x0)

        >> print(lagrange_interpol(xi, yi, x0, False))

        3.0


    :param xi: Conjunto de puntos xi (List[float])
    :param yi: Conjunto de puntos yi (List[float])
    :param x0: Aproximación de la función en un punto determinado x0 (float)
    :param simbolico: Determina si se realizará por cálculo simbólico (sin resultado numérico) o no (bool)
    """

    if len(xi) != len(yi):
        raise ValueError("Conjuntos de puntos de diferentes tamaños")
    resultado = 0
    a = x
    if not simbolico:
        a = x0

    for i in range(len(xi)):
        l = 1

        for j in range(len(xi)):
            if j != i:
                l = l * ((a - xi[j]) / (xi[i] - xi[j]))

        resultado = resultado + l * yi[i]

    return resultado
