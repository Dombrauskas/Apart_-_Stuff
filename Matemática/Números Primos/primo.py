"""
 " 
 " autor Maurício Freire
 " Números Primos.
 " Prime Numbers.
"""
n =  int(input())
primos = 0

for i in range(n, 0, -1):
    # Avalia as divisões possíveis (que não deixam resto).
    # Apprizes the possible divisions (with no remainder).
    res = n % i
    if res == 0:
        primos += 1
        # Se houver mais de duas divisões exatas o número não é primo.
        # Having more than two exacts division the number is not prime.
        if primos > 2:
            break

if primos == 2:
    print(n, "é primo!")
else:
    print(n, "não é primo")

