'''
 '
 ' autor Maurício Freire
 ' A Conjectura de Goldbach diz que todo número par maior que 2 pode ser obtido pela
 ' soma de dois números primos inferiores a ele.
 ' The Goldbach's Conjecture says that any even number greater than 2 may be written
 ' as the sum of two prime numbers.
'''

'''
 ' Preenche um vetor com todos os números primos dentro do limite escolhido.
 ' Fill an array with all the prime numbers within the chosen boundaries.
'''
def primos(p):
    x = 0
    c = x
    v = []
    for n in range(1,p+1):
        for j in range(1,p+1):
            if n % j == 0:
                x += 1
        if x <= 2:
            v += [n]
        x = 0
    print("Números primos entre 1 e", p,":")
    print(v)
    Goldbach(v, p)

'''
 ' Função para encontrar uma soma possível (pode haver mais de uma) de
 ' primos para formar a expressão.
 ' Function to encounter a possible sum (there might have more than one)
 ' of primes to make the expression.
'''
def Goldbach(v, p):
    g = (int(input("\nDigite um número inferior a ")))
    print(p, ">>>", g)
    
    # Evita escolha de números superiores ao maior primo.
    # Avoid choosing numbers greater than the largest prime.
    if g > p:
        while g > p:
            g = (int(input("Digite um número inferior a ")))
            print(p, ">>>", g)
    
    # Decrementa um se o número for ímpar.
    # If the number is odd it is decremented by one.
    if g % 2 != 0:
        g -= 1
    
    # Elege o maior primo abaixo do número escolhido.
    # Elect the greater prime under the number chosen.
    for i in range(g):
        if v[i] > g:
            i -= 1
            break
    
    # Exibe as somas possíveis.
    # Shows the possible sums.
    for j in range(0,i):
        for k in range(0,i+1):
            if v[j] + v[k] == g:
                print(v[j], "+", v[k], "=", g)
                
p = (int(input("Digite um número: ")))
print(p,"\n")
primos(p)
