"""
 "
 " @autor Maurício Freire
 " Mostra a representação binária de um dado número.
 " Shows the binary representation of a chosen number.
"""

n = (int(input("Digite um número: ")))
bin = []

# Converte o número digitado para 0 e 1.
# Convertes the typed number in 0 and 1.
print(n,"em binário é: ", end="")
for i in range(16):
    if n % 2 == 0:
        bin.append(0)
        n = (int) (n / 2)
    else:
        bin.append(1)
        n = (int) (n / 2)

# Exibe a representação binária do número
# Shows the binary representation of the number.
for i in range(15,-1,-1):
    print(bin[i], end="")
    if i % 8 == 0:
        print(" ", end="")
