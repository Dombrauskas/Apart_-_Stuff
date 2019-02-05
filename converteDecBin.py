'''
 '
 ' @autor Mauricio Maurício Freire
 ' Mostra a representação binária de um dado número.
 ' Shows the binary representation of a chosen number.
'''

n = (int(input("Digite um número: ")))
bin = []

print(n,"em binário é: ", end="")
for i in range(16):
    if n % 2 == 0:
        bin.append(0)
        n = (int) (n / 2)
    else:
        bin.append(1)
        n = (int) (n / 2)

for i in range(15,-1,-1):
    print(bin[i], end="")
    if i % 8 == 0:
        print(" ", end="")
