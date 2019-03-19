"""
 "
 " Autor Maurício Freire
 " Métoda da Posição Falsa (Secante)
 " False Position Method (Secant)
"""

import math
from math import cos as C
from math import log as ln

def Xn(a, b, fa, fb):
    xn = ((a * fb - b * fa) / (fb - fa))
    if xn > 0:
        raiz(xn, b)
    else:
        raiz(a, xn)

# Calcula os valores de f(a) e f(b).
# Calculate the values of f(a) e f(b).
def raiz(x, y):
    fx = C(x * 3) - ln(x - 3)
    fy = C(y * 3) - ln(y - 3)
    print("{} {}".format(fx, fy))

    try:
        assert fx < 0 and fx > 0
        Xn(x, y, fx, fy)
    except:
        Xn(y, x, fy, fx)
        #print("Ocorreu um erro durante a execução!")

a = int(input("Intervalo: "))
b = int(input("Intervalo: "))

raiz(a, b)