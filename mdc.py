'''
 '
 ' autor Maurício Freire
 ' Cálculo do Máximo Divisor Comum consiste em encontrar o maior termo comum a
 ' dois (ou mais) números capaz de dividir ambos.
 ' Calcule of the Greatest Common Divisor consists in finding the greatest value
 ' common to two (or more) number that is able to divide both.
'''

def mdc(x, y):
    # Define o maior número.
    # Define the highest number.
    if x > y:
        mx = x
        mn = y
    elif x < y:
        mx = y
        mn = x
    else:
        print('Informe números diferentes!')
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
            print("Mdc {}".format(mn))
    except ZeroDivisionError:
        print("Mdc {}".format(mn))

# Impede a escolha de dois números iguais.
# Prevents the usage of two equal numbers.
e = True
while e:
    s = int(input())
    r = int(input())

    e = mdc(s, r)
