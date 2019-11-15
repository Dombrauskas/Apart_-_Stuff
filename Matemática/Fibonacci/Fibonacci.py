"""
 " 
 " author Maurício
 " Calcula a seqüência de Fibonacci até o número escolhido.
 " Calculates the Fibonacci sequence until a chosen number.
"""

def fib(x):
    a = b = c = 1
    while c < x:
        if b == 1:
            print(a, b)
        c = b + a
        a = b
        b = c
        print(c)
    

x = int(input("Informe um numero: "))
fib(x)

