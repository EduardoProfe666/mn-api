from sympy import symbols
from sympy.plotting import plot
import math

x = symbols('x')

# Datos
f = (math.e**-x)-x

# Graficado
p = plot(f, (x, 0, 1))