"""
 "
 " Autor Maurício Freire
 " Cálculo do Máximo Divisor Comum consiste em encontrar o maior termo comum a
 " dois (ou mais) números capaz de dividir ambos.
 " Calcule of the Greatest Common Divisor consists in finding the greatest value
 " common to two (or more) number that is able to divide both.
"""

def mdc(x, y):
    # Impede a seleção de números iguais ou negativos.
    # Prevents the choice of equal or negative numbers.
    if x < 0 or y < 0:
        print("Impossível calcular o MDC!")
        x = y
        
    # Define o maior número, ou os define como iguais.
    # Define the highest number, or define them as equals.
    if x > y:
        mx = x
        mn = y
    elif x < y:
        mx = y
        mn = x
    else:
        print('Informe números diferentes!\n')
        return True
    
    # Evita uma possível divisão por zero.
    # Avoid a possible ZeroDivisionError.
    try:
        a = int(mx / mn)
        b = mx % mn
        #print("{} / {} = {}".format(mx,mn,b))
        # Se b for diferente de zero o MDC ainda não alcançado.
        # If b is non-zero the GCD has not been reached yet.
        if b != 0:
            mdc(mn, b)
        else:
            print("MDC {}".format(mn))
    except ZeroDivisionError:
        print("MDC não existe!")

e = True
while e:
    # Garante que sejam informados apenas inteiros.
    # Ensures that just integers to be informed.
    try:
        s = int(input('Informe o 1º número: '))
        r = int(input('Informe o 2º número: '))
        e = mdc(s, r)
    except ValueError:
        print("Informe números inteiros apenas!")
        e = True
