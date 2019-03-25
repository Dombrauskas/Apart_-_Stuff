"""
 "
 " Autor Maurício Freire
 " Método da Posição Falsa (Secante)
 " False Position Method (Secant)
"""

import math
from math import cos as C
from math import log as ln

def Xn(a, b, fa, fb, n, p):
    xn = ((a * fb - b * fa) / (fb - fa))
    fxn = C(xn * 3) - ln(xn - 3)

    # Chamar o critério de parada antes de chamar a raiz outra vez.
    # Ainda pensando em como definir a substituição de a ou b por xn.
    erro(fxn, xn)
    
    if xn < 0:
        raiz(xn, p)
    else:
        raiz(n, xn)

# Estabelece o critério de parada.
# Establishes the ending criterion.
def erro(fxn, xn):
    E = 10**-2
    m = (fxn + E) * (fxn - E)
    if (m < E):
        print("\nRaiz encontrada: {}".format(xn))
        raise Exception
   
# Calcula os valores de f(a) e f(b).
# Calculate the values of f(a) e f(b).
def raiz(x, y):
    fx = C(x * 3) - ln(x - 3)
    fy = C(y * 3) - ln(y - 3)
        
    if fx < 0 and fy > 0:
        Xn(x, y, fx, fy, x, y)
    else:
        Xn(x, y, fx, fy, y, x)

a = int(input("Intervalo A: "))
b = int(input("Intervalo B: "))

try:
    raiz(a, b)
except:
    print()
