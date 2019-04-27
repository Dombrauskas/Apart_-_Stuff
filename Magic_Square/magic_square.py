"""
 " 
 " autor Maurício Freire
 " Quadrado Mágico: a soma dos números da primeira linha, da diagonal principal
 " e a da coluna à esquerda devem ser iguais.
 " Magic Square: the sum of the numbers in the first line, the main diagonal and
 " the left column must be the same.
"""

#import random
def magic_square(matriz):
    q = w = 0
    dia = lin = col = 0
    
    #Soma a 1ª linha, a diagonal principal e a coluna esquerda.
    #Sum up the 1st line, the main diagonal and the left column.
    for i in matriz:
        for j in matriz[q]:
            if q == 0:
                lin += j
            if w == 0:
                col += j
            if q == w:
                dia += j
            print(j, end=" ")
            w += 1
        print()
        q += 1
        w = 0
    if dia == lin and lin == col:
        print("You got a 'Magic Square!'")
    else:
        print("It is not a Magic Square!")
    print()
    print(dia, lin, col)

y = n = int(input("Qual tamanho da matriz deseja criar? "))
mat = []

#Preenche a matriz.
#Fill the matrix up.
while y > 0:
    vet = []
    for i in range(n):
        x = int(input())
        vet.append(x)#random.randint(0,9))
    mat.append(vet)
    y -= 1
print(mat)

magic_square(mat)
