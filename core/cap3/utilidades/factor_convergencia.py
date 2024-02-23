"""
Capítulo 3. Utilidades. Factor de convergencia.
Módulo que provee de los principales algoritmos relacionados con el
factor de convergencia.
"""
from numpy import absolute


def hallar_factor_convergencia_alfa(a):
    """
     Descripción:
     -----------------
     Permite hallar el factor de convergencia α de la matriz A

     Parámetros:
     ----------------
         a: array de numpy que representa la matriz de los coeficientes A (AX=B)

     Salida:
     --------------
         number: número que representa el factor de convergencia α

     Ejemplo:
     --------------
         >> from numpy import array

         >> a = array([[5, -1, 1],
            [2, 5, -1],
            [-1, 1, 5]])

         >> print(f'El factor de convergencia α es {hallar_factor_convergencia_alfa(a)}')

         >> El factor de convergencia α es 0.6

     :param a: Array de numpy que representa la matriz de los coeficientes A (AX=B)
     """
    a = absolute(a)
    resultado = []

    for i in range(len(a)):
        total_fila = sum(a[i])

        if total_fila - a[i][i] < 0:
            raise Exception("El factor de convergencia de la matriz tiene que ser mayor que 0")

        resultado.append((total_fila - a[i][i]) / a[i][i])

    return max(resultado)


def hallar_factor_convergencia_beta(a):
    """
    Descripción:
    -----------------
    Permite hallar el factor de convergencia β de la matriz A

    Parámetros:
    ----------------
        a: array de numpy que representa la matriz de los coeficientes A (AX=B)

    Salida:
    --------------
        number: número que representa el factor de convergencia β

    Ejemplo:
    --------------
        >> from numpy import array

        >> a = array([[5, -1, 1],
           [2, 5, -1],
           [-1, 1, 5]])

        >> print(f'El factor de convergencia β es {hallar_factor_convergencia_beta(a)}')

        >> El factor de convergencia β es 0.4

    :param a: Array de numpy que representa la matriz de los coeficientes A (AX=B)
    """
    a = absolute(a)
    resultado = []

    for i in range(a.shape[0]):
        total_fila = sum(a[i])

        if total_fila - a[i][i] < 0:
            raise Exception("El factor de convergencia de la matriz tiene que ser mayor que 0")

        q = 0
        p = 0
        for j in range(a.shape[1]):
            if i > j:
                p += a[i][j] / a[i][i]
            elif i < j:
                q += a[i][j] / a[i][i]

        resultado.append(q / (1 - p))

    return max(resultado)


def hallar_f_convergencia_error(f_convergencia):
    """
    Descripción:
    -----------------
    Permite determinar el error del factor de convergencia

    Parámetros:
    ----------------
        f_convergencia: número que representa el factor de convergencia

    Salida:
    --------------
        number: número que representa el error del factor de convergencia

    Ejemplo:
    --------------
        >> f_convergencia = 0.4

        >> print('error = {:.5f}\n'.format(hallar_f_convergencia_error(f_convergencia)))

        >> error = 0.66667

    :param f_convergencia: Número que representa el factor de convergencia
    """
    return abs(f_convergencia / (1 - f_convergencia))
